import pandas as pd
import os
import shutil
def datasetCutter(filepath: str):
    # Wczytaj plik and Zamień na wielki dataset
    df = pd.read_csv(filepath, sep=';', skiprows=4, decimal=',')#, low_memory=False)
    #'fullFiles/Michal/Triceps.csv'
    df = df.drop('Time,s', axis=1)
    # Ustal ścieżkę, gdzie pliki będą zapisywane
    outDir = './dir'
    if os.path.exists(outDir):
        shutil.rmtree(outDir)
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
    maxSize = 0
    fileSize = 1500
    index_list = []
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
            # #name of file
            # name +=1
            # print(name)
            start = index
        #zapisa jednego ruchu
        if pastFlag == True and flag == False:
            end = index
            index_list.append((start,end))
    # for start, end in index_list:
    #     if (maxSize < end-start):
    #         maxSize = end-start
    for start, end in index_list:
        if (end-start > 500):
            # name of file
            name += 1
            nDF = df.loc[start:start+fileSize].copy()
            new_index = []
            for i in range(0,nDF.size):
                new_index.append(i)
            nDF.reset_index(drop=True, inplace=True)
            filename = str(name) + ".csv"
            fullname = os.path.join(outDir, filename)
            nDF.to_csv(fullname, sep=';')
    #print(index)
    # Jeśli flag == true and MV > treshold -> append new row in dataset


