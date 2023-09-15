import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
file_path = "Demand_LOI.csv"
df = pd.read_csv(file_path)

# Assuming you have two columns in your CSV that you want to analyze
column1 = "Count Legal Tickets"  # Replace with the actual column name
column2 = "LOI Count"  # Replace with the actual column name

# Check if the columns exist in the DataFrame
if column1 in df.columns and column2 in df.columns:
    # Extract the relevant columns as NumPy arrays
    series1 = df[column1].values
    series2 = df[column2].values

    # Calculate cross-correlation with lags
    max_lag = len(series1) - 1
    cross_correlation = []

    for lag in range(-max_lag, max_lag + 1):
        if lag < 0:
            corr = np.corrcoef(series1[:lag], series2[-lag:])[0, 1]
        elif lag == 0:
            corr = np.corrcoef(series1, series2)[0, 1]
        else:
            corr = np.corrcoef(series1[lag:], series2[:-lag])[0, 1]
        cross_correlation.append(corr)

    # Create an array of lags
    lags = np.arange(-max_lag, max_lag + 1)

    # Plot the cross-correlation
    plt.figure(figsize=(10, 4))
    plt.plot(lags, cross_correlation, marker='o', linestyle='-', color='b')
    plt.xlabel('Lag')
    plt.ylabel('Cross-Correlation')
    plt.title('Cross-Correlation Analysis')
    plt.grid(True)
    plt.show()
else:
    print(f"Columns '{column1}' and '{column2}' not found in the CSV file.")
