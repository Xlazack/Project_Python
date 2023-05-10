import pandas as pd
import os

# Wczytaj plik and Zamień na wielki dataset
df = pd.read_csv('fullFiles/Maciek/Stak lokciowy wyprost, nadgarstkowy wyprost.csv', sep=';', skiprows=4, decimal=',')#, low_memory=False)
df = df.drop('Time,s', axis=1)
# Ustal ścieżkę, gdzie pliki będą zapisywane
outDir = "./dir"
if not os.path.exists(outDir):
    os.mkdir(outDir)
# Deklaracja Tresholda
treshold = 12
# Deklaracja flagi i pastFlagi
pastFlag = False
flag = False
name = 0
start = 0
end = 0
# Iteruj po całym datasecie
for index, rows in df.iterrows():
    #pastFlag = flag
    pastFlag = flag
    # Sprawdzaj max Value
    maxValue = max(rows[0], rows[1], rows[2], rows[3])
    #print(maxValue)
    # Porównaj max Value do tresholda
    if maxValue > treshold:
        # Jeśli MV > treshold -> flag = true
        flag = True
    # Jeśli MV not > treshold -> flag = false -> zapisz nowy dataset jako nowy plik
    if maxValue <= treshold:
        flag = False
    # Jeśli pastFlag == false and flag == true create new dataset
    if pastFlag == False and flag == True:
        #name of file
        name +=1
        print(name)
        filename = str(name) + ".csv"
        start = index
    #zapisa jednego ruchu
    if pastFlag == True and flag == False:
        end = index
        nDF = df.loc[start:end].copy()
        new_index = []
        for i in range(0,nDF.size):
            new_index.append(i)
        nDF.reset_index(drop=True, inplace=True)
        fullname = os.path.join(outDir, filename)
        nDF.to_csv(fullname, sep=';')
#print(index)
# Jeśli flag == true and MV > treshold -> append new row in dataset


