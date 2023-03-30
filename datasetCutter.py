import pandas as pd

# specify the data types for columns 0 to 4
dtypes = {'Column0': float, 'Column1': float, 'Column2': float, 'Column3': float, 'Column4': float}

# Read the CSV file
df = pd.read_csv('Zgiecie nadgarstka.csv', sep=';', skiprows=3, decimal=',', dtype=dtypes)

# Print the DataFrame
print(df)