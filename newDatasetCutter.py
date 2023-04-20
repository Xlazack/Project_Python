import pandas as pd


#Wczytaj plik and Zamień na wielki dataset
df = pd.read_csv('Zgiecie nadgarstka.csv', sep=';', skiprows=4, decimal=',', low_memory=False)

#Deklaracja Tresholda
treshold = 2
#Deklaracja flagi i pastFlagi
pastFlag = False
flag = False
#Iteruj po całym datasecie
for rows in df.iterrows:
    # Sprawdzaj max Value
    maxValue = max(rows[0], rows[1], rows[2], rows[3])
    #Porównaj max Value do tresholda
    if maxValue > treshold:
        # Jeśli MV > treshold -> flag = true
        flag = True


#Jeśli pastFlag == false and flag == true create new dataset

#Jeśli flag == true and MV > treshold -> append new row in dataset

#Jeśli MV not > treshold -> flag = false -> zapisz nowy dataset jako nowy plik