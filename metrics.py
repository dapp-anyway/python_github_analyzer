from pathlib import Path
from config import STATS_DIR, STATS_RESULTS_DIR
from utils import create_folder
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import pprint as pp
import shutil
import json
import os


# Calculates the Spearman correlation matrix for the data in the CSV file
# Converts the upper triangle of the correlation matrix into a single row
# Assigns labels to each value in the row in the format "metric_a x metric_b"
# Adds the sample size as the first column in the row
# Converts the row to a DataFrame
# Returns the DataFrame representing the correlation row
def generate_correlation_row_from_csv(path):
    f = pd.read_csv(path)
    n = len(f.index)

    corr = generate_correlation_matrix_from_csv(path)

    corr_len = len(corr.index)
    if corr_len == 0:
        return -1
    else:
        row = corr.iloc[0, 1:]
        for i in range(1, corr_len - 1):
            row = pd.concat([row, corr.iloc[i, i + 1:]], ignore_index=True)
        index = generate_index(corr.columns.values)
        row = row.rename(lambda x: index[x])
        n_data = pd.Series(data={'n': n}, index=['n'])
        row = pd.concat([n_data, row])
        row = row.to_frame().transpose()
        return row


# Calculates the Spearman correlation matrix for the data in the CSV file
# Converts the upper triangle of the correlation matrix into a DataFrame
# Returns the correlation matrix
def generate_correlation_matrix_from_csv(path):
    csv = pd.read_csv(path)
    spearman = csv.corr(method='spearman')
    correlation_matrix = pd.DataFrame(np.triu(spearman), index=spearman.columns, columns=spearman.columns)
    return correlation_matrix

# Generates all possible combinations of labels as pairs (excluding self-pairing)
# Returns a list of strings representing the pairs in the format "label_a x label_b"
def generate_index(labels):
    ls_pairs = []
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            ls_pairs.append(f"{labels[i]} x {labels[j]}")
    return ls_pairs


# Iterates over all CSV files in the directory
def concat_project_stats_to_results(project_result_path):
    for csv_path in Path(project_result_path).rglob('*.csv'):
        file_type = get_file_type(csv_path)
        dist = f"./{STATS_DIR}/{STATS_RESULTS_DIR}/{file_type}.csv"
        try:
            f = concat_correlation_rows(dist, csv_path)
            f.to_csv(dist, index=False)
        except:
            create_folder(f"./{STATS_DIR}/{STATS_RESULTS_DIR}")
            shutil.copy(csv_path, dist)


# Concatenates the two DataFrames vertically
# Returns the concatenated DataFrame
def concat_correlation_rows(path1, path2):
    data1 = pd.read_csv(path1)
    data2 = pd.read_csv(path2)
    data = pd.concat([data1, data2])
    return data

# Extracts the file type from the file name
def get_file_type(path):
    filename = os.path.basename(path)
    name = filename.split('.csv')[0]
    return name.split('-')[-1]

# Analyze single repository
def analyze_repository(path, project_name):
    create_folder(f'{STATS_DIR}/{project_name}')
    for csv_path in Path(path).rglob('*.csv'):
        corr = generate_correlation_row_from_csv(csv_path)
        if type(corr).__name__ == 'int':
            continue
        corr.to_csv(f'{STATS_DIR}/{project_name}/{csv_path.name}', index=False)
