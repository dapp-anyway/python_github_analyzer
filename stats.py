from config import STATS_DIR, STATS_RESULTS_DIR
from pathlib import Path
from statsmodels.stats.weightstats import DescrStatsW
import pandas as pd
import numpy as np

# Adds statistical values to each CSV file in the specified directory
def add_stats_values_in_csv():
    components_path = f"./{STATS_DIR}/{STATS_RESULTS_DIR}"
    # components_path = f"./test_meta/{STATS_RESULTS_DIR}"
    # Iterate over all CSV files in the directory and its subdirectories
    for path in Path(components_path).rglob('*.csv'):
        path = str(path)
        data = pd.read_csv(path)
        # Get statistical values for the data
        stats = calculate_stats(data)
         # Concatenate the original data and the statistical values
        data = pd.concat([data, stats])
        # Save the correlation matrix to a new CSV file with postfix __S
        new_file = f"{path.split('.csv')[0]}__S.csv"
        data.to_csv(new_file)

# Calculates statistics for the given data
def calculate_stats(data):
    k = len(data.index)
    samples = data.loc[:, 'n']
    # Initialize result dictionary to store calculated statistics
    result = {'theta': [], 'p': [], 'se': [], 'll': [], 'ul': []}

    # Iterate over each column in the data DataFrame
    for column in data.columns:
        if column != 'n':
            correlations = data.loc[:, column]
            p_data = pd.concat([samples, correlations], axis=1)
            p_data = p_data.dropna(axis=0)
            p_samples = np.array(p_data.iloc[:, 0])
            p_correlations = np.array(p_data.iloc[:, 1])
            # Check if there are any valid data points
            if len(p_correlations) == 0:
                NaN = np.nan
                stats = [NaN, NaN, NaN, [NaN, NaN], [NaN, NaN]]
            else:
                # Calculate statistics using weighted DescrStatsW
                ds = DescrStatsW(p_correlations, weights=p_samples)
                mean = ds.mean
                p = np.tanh(mean)
                se_re = ds.std_mean
                LL = ds.tconfint_mean()[0]
                UL = ds.tconfint_mean()[1]
                stats = [mean, p, se_re, [LL, LL], [UL, UL]]
            
            # Append calculated statistics to the result dictionary
            result['theta'].append(stats[0])
            result['p'].append(stats[1])
            result['se'].append(stats[2])
            result['ll'].append(stats[3][1])
            result['ul'].append(stats[4][1])
    
    # Create a new DataFrame from the calculated statistics
    new_data = pd.DataFrame([result['theta'], result['p'], result['se'], result['ll'], result['ul']])
    index = data.columns.values[1:]
    new_data = new_data.rename(lambda x: index[x], axis='columns')
    new_data = new_data.rename(lambda x: ['theta', 'p', 'se', 'll', 'ul'][x], axis='rows')
    return new_data


# add_stat_values_in_csv()