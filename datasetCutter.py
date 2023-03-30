import pandas as pd

# Read the CSV file
df = pd.read_csv(r'/home/xlazack/Documents/Kazalski/Zgiecie nadgarstka.csv', sep=';', skiprows=4, decimal=',', low_memory=False)

# Print the DataFrame
print(df)

#defining splitting argument
grouped = df.groupby('column_name')

#splitting a file
for name, group in grouped:
    filename = name + '.csv'
    group.to_csv(filename, index=False)
