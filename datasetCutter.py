import pandas as pd

# Read the CSV file
df = pd.read_csv('Zgiecie nadgarstka.csv', sep=';', skiprows=4, decimal=',', low_memory=False)

# Uzyskaj liczbę wierszy w oryginalnym pliku
total_rowes = df.shape[0]

# Oblicz liczbę wierszy w każdym pliku
rows_per_file = total_rowes // 50

# Podziel oryginalny plik na 50 mniejszych
i = 0
start_index = 0
for index, row in df.iterrows():
    if row['FLEX.CAPR.U RT,%'] > 1.5:
        # Utwórz nowy DataFrame dla każdego pliku
        new_df = df.iloc[start_index:index]

        # Zapisz nowy plik CSV
        new_df.to_csv(f'mały_plik_{i}.csv', index=False)

        # Przejdź do kolejnego pliku
        i += 1
        start_index = index

# Utwórz i zapisz ostatni plik CSV
new_df = df.iloc[start_index:]
new_df.to_csv(f'mały_plik_{i}.csv', index=False)



# Print the DataFrame
print(df)