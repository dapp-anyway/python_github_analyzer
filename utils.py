from config import STATS_RESULTS_DIR, STATS_DIR
from pathlib import Path
import pandas as pd
import os
import re

# Check for correct GitHub link
def is_valid_github_link(link):
    pattern = r'^https?://github\.com/.+/.+$'
    match = re.match(pattern, link)
    return match is not None

# Create an empty folder if there is none
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Remove empty columns and rows in single file
def remove_empty_lines_file(path):
    df = pd.read_csv(path, index_col=0)
    df = df.dropna(axis=0, how='all')
    df = df.dropna(axis=1, how='all')
    return df

# Remove empty columns and rows in statistic result files
def remove_empty_lines():
    dir_path = f"{STATS_DIR}/{STATS_RESULTS_DIR}"
    for csv_path in Path(dir_path).rglob('*.csv'):
        df = remove_empty_lines_file(csv_path)
        df.to_csv(csv_path)
