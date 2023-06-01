import numpy as np
import pandas as pd
import os
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from functions import loadFiles
from functions import createNN
from functions import useModel

# Define the input shape of the data
input_shape = (6004,)  # 4 channels

# Define the number of possible classes
num_classes = 8  # 8 signal shapes

# Define the batch size and number of epochs for training
batch_size = 32
epochs = 100

# Define the path to the folders containing the signal files
signal_folders = ["NTF/1", "NTF/2", "NTF/3", "NTF/4", "NTF/5", "NTF/6", "NTF/7", "NTF/8"]

loadFiles(num_classes, signal_folders)

createNN(input_shape, num_classes, batch_size, epochs)

useModel("NTF/3/21.csv")
