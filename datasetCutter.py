import pandas as pd

# Read the CSV file
df = pd.read_csv('Zgiecie nadgarstka.csv', sep=';', skiprows=4, decimal=',', low_memory=False)

# Print the DataFrame
print(df)