from config import STATS_DIR, STATS_RESULTS_DIR
from pathlib import Path
import pandas as pd
import numpy as np
import math 


# This function creates correlation files for each CSV file in the specified directory
def create_correlation_files():
    # Define the directory path where the CSV files are located
    components_path = f"./{STATS_DIR}/{STATS_RESULTS_DIR}"
    # components_path = f"./test_meta/{STATS_RESULTS_DIR}"

    # Iterate over all CSV files in the directory and its subdirectories
    for path in Path(components_path).rglob('*__S.csv'):
        path = str(path)
        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv(path, index_col=0)
        # Calculate the correlation matrix from the 'p' in the DataFrame
        corr: pd.DataFrame = create_correlation_matrix(data.loc['p'])
        # Save the correlation matrix to a new CSV file with postfix __C
        new_file = f"{path.split('__S.csv')[0]}__C.csv"
        corr.to_csv(new_file)

# Creates a correlation matrix
def create_correlation_matrix(series):
    series = series.iloc[1:]
    index = series.index
    series.reset_index(drop=True, inplace=True)
    len_m = round((1 + math.sqrt(1 + (8) * len(index))) / 2)
    data = pd.DataFrame()
    for i in range(len_m - 1):
        x, inc_i = len_m, i + 1
        interval = list(map(lambda k: int(k * (x - (k + 1) / 2)), [i, inc_i]))
        series_as_row = series.iloc[interval[0]:interval[1]].to_frame().T
        series_as_row = series_as_row.rename(lambda a: a - interval[0] + i, axis='columns')
        data = pd.concat([data, series_as_row], axis=0, ignore_index=True)
    empty = pd.DataFrame(np.nan, index=range(len_m), columns=['A'])
    data = pd.concat([empty, data], axis=1, ignore_index=True)
    get_correlated_name = lambda index_val: index_val.split(' x ')[1]
    correlated_names = list(map(get_correlated_name, index))
    metric_names = [index[0].split(' x ')[0]] + correlated_names
    data = data.rename(lambda a: metric_names[a])
    data = data.rename(lambda a: metric_names[a], axis=1)
    return data


# create_correlation_files()