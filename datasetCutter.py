import pandas as pd
from sklearn.model_selection import train_test_split

# wczytanie danych z pliku CSV
data = pd.read_csv("MVC 17.03.csv")

# podział danych na zbiór treningowy i testowy
train_data, test_data = train_test_split(data, test_size=0.2)

# zapisanie podzielonych danych do plików CSV
train_data.to_csv("nazwa_pliku_treningowego.csv", index=False)
test_data.to_csv("nazwa_pliku_testowego.csv", index=False)
