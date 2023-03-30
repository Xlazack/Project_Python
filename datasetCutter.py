import pandas as pd

# Read the CSV file
df = pd.read_csv('Zgiecie nadgarstka.csv', sep=';', skiprows=3, decimal=',')

# Print the DataFrame sadadlkn
print(df)