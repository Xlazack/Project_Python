import pandas as pd

# Wczytaj plik and Zamień na wielki dataset
df = pd.read_csv('Zgiecie nadgarstka.csv', sep=';', skiprows=4, decimal=',')#, low_memory=False)
print(df)
df = df.drop('Time,s', axis=1)
print(df)
# Deklaracja Tresholda
treshold = 15
# Deklaracja flagi i pastFlagi
pastFlag = False
flag = False
name = 0
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
        print("Ping")
        name +=1
        print(name)
        filename = str(name) + ".csv"
        #nie działa nDF = pd.DataFrame({'name':['FLEX.CAPR.U RT,%', 'BICEPS BR. RT,%', 'BRACHIORAD. RT,%',  'LAT. TRICEPS RT,%']})

    #Zostało wpisywać row z df do nowego dataframu który będzie zapisany do pliku

    if maxValue > treshold:
        row = df.iloc[index]
        nDF = nDF.append(row)
    if pastFlag == True and flag == False:
        nDF.to_csv(filename, sep=';')
#print(index)
# Jeśli flag == true and MV > treshold -> append new row in dataset


