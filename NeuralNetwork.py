import numpy as np
import pandas as pd
import os
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

# Define the input shape of the data
input_shape = (6004,) # 4 channels

# Define the number of possible classes
num_classes = 8 # 8 signal shapes

# Define the batch size and number of epochs for training
batch_size = 32
epochs = 100

# Define the path to the folders containing the signal files
signal_folders = ["NTF/1", "NTF/2", "NTF/3", "NTF/4", "NTF/5", "NTF/6", "NTF/7", "NTF/8"]

# Load the data into memory
data = []
labels = []
for i, folder in enumerate(signal_folders):
    file_names = os.listdir(folder)
    for file_name in file_names:
        file_path = os.path.join(folder, file_name)
        df = pd.read_csv(file_path, delimiter=";", decimal=",", header=None)
        df = df.iloc[1:, 1:] # remove the index column and headers
        signal = df.values.reshape(-1)
        data.append(signal)
        labels.append(i)

# Convert the data and labels to numpy arrays
data = np.array(data)
labels = np.array(labels)

# Split the data and labels into training and testing sets
indices = np.random.permutation(len(data))
split_index = int(0.8 * len(data))
train_indices, test_indices = indices[:split_index], indices[split_index:]
x_train, y_train = data[train_indices], labels[train_indices]
x_test, y_test = data[test_indices], labels[test_indices]

# Preprocess the data
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 100 # normalize the data
x_test /= 100

# Convert the labels to one-hot encoding
y_train = np.eye(num_classes)[y_train]
y_test = np.eye(num_classes)[y_test]

# Define the neural network model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=input_shape))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
sgd = SGD(learning_rate=0.01, momentum=0.9, decay=1e-6, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test))

# Evaluate the model on the testing set
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Use the model to predict new data
new_data = pd.read_csv("NTF/3/20.csv", delimiter=";", decimal=",", header=None)
new_data = new_data.iloc[1:, 1:] # remove the index column and headers
new_signal = new_data.values.reshape(-1)
new_signal = new_signal.astype('float32')
new_signal /= 100 # normalize the data
new_signal = np.array([new_signal])
prediction = model.predict(new_signal)
predicted_class = np.argmax(prediction)
print('Predicted class:', predicted_class + 1)
print('Predictions:', prediction)
