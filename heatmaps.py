import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the xlsx file
file_path = "heatmaps/Metrics Correlations.xlsx"
xlsx = pd.ExcelFile(file_path)

# Read and process each sheet
for sheet_name in xlsx.sheet_names:
    # Load data from the current sheet
    df = xlsx.parse(sheet_name)

    # Use the first column and first row as metric names
    metrics = df.iloc[0:, 0].tolist()  # Row indices with metrics
    values = df.columns.to_list()[1:]  # Column indices with values

    print(metrics)
    print(values)

    # Create the data matrix for the heatmap
    data = df.iloc[0:, 1:].astype(float)

    # Create the heatmap
    plt.figure(figsize=(13, 11))
    cmap = sns.color_palette("binary", as_cmap=True)
    sns.heatmap(data, cmap=cmap, cbar=True, xticklabels=values, yticklabels=metrics)
    plt.title(sheet_name)

    # Save the heatmap to a file
    output_path = f"heatmaps/hm_{sheet_name}.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.close()

    print(f"Heatmap for sheet '{sheet_name}' saved to file '{output_path}'")
