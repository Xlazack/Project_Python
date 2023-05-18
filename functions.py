import numpy as np
import pandas as pd
import os
from keras.models import Sequential
from keras.layers import Dense, Dropout
import tensorflow as tf
from keras.optimizers import SGD
def loadFiles(num_classes: int = 8, signal_folders = ["NTF/1", "NTF/2", "NTF/3", "NTF/4", "NTF/5", "NTF/6", "NTF/7", "NTF/8"]):
    # Load the data into memory
    data = []
    labels = []
    for i, folder in enumerate(signal_folders):
        file_names = os.listdir(folder)
        for file_name in file_names:
            file_path = os.path.join(folder, file_name)
            df = pd.read_csv(file_path, delimiter=";", decimal=",", header=None)
            df = df.iloc[1:, 1:]  # remove the index column and headers
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
    global x_train, y_train
    global  x_test, y_test
    x_train, y_train = data[train_indices], labels[train_indices]
    x_test, y_test = data[test_indices], labels[test_indices]

    # Preprocess the data
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 100  # normalize the data
    x_test /= 100

    # Convert the labels to one-hot encoding
    y_train = np.eye(num_classes)[y_train]
    y_test = np.eye(num_classes)[y_test]


def createNN(input_shape = (6004,), num_classes: int = 8, batch_size: int = 32, epochs: int = 100):
    # Define the neural network model
    global model
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=input_shape))
    model.add(Dropout(0.5))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    # Compile the model
    sgd = tf.keras.optimizers.legacy.SGD(learning_rate=0.01, momentum=0.9, decay=1e-6, nesterov=True)

    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test))

    # Evaluate the model on the testing set
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

def useModel(pathfile: str):
    # Use the model to predict new data
    new_data = pd.read_csv(pathfile, delimiter=";", decimal=",", header=None)
    new_data = new_data.iloc[1:, 1:]  # remove the index column and headers
    new_signal = new_data.values.reshape(-1)
    new_signal = new_signal.astype('float32')
    new_signal /= 100  # normalize the data
    new_signal = np.array([new_signal])
    global predicted_class
    prediction = model.predict(new_signal)
    predicted_class = np.argmax(prediction)
    print('Predicted class:', predicted_class + 1)
    print('Predictions:', prediction)
    return predicted_class+1