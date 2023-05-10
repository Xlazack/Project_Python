import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Define a function to load a CSV file as a numpy array
def load_csv_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines[1:]:
        row = [float(x) for x in line.strip().split(';')[1:]]
        data.append(row)
    return np.array(data)

# Define a function to load all CSV files in a directory as a list of numpy arrays
def load_csv_files(directory_path):
    files = os.listdir(directory_path)
    data = []
    for file in files:
        file_path = os.path.join(directory_path, file)
        data.append(load_csv_file(file_path))
    return data

# Define a function to load all CSV files in all directories as a list of numpy arrays
def load_data(base_path):
    classes = os.listdir(base_path)
    x = []
    y = []
    for i, cls in enumerate(classes):
        class_path = os.path.join(base_path, cls)
        class_data = load_csv_files(class_path)
        x += class_data
        y += [i] * len(class_data)
    return x, y

# Load the data
base_path = 'C:\Users\macie\PycharmProjects\Project_Python\TF'
x, y = load_data(base_path)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Convert the data to numpy arrays
x_train = [np.array(d) for d in x_train]
x_test = [np.array(d) for d in x_test]
y_train = np.array(y_train)
y_test = np.array(y_test)

# Pad or truncate the sequences to a fixed length
max_length = 1000
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=max_length, dtype='float32')
x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=max_length, dtype='float32')

# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(max_length, x_train[0].shape[1])),
    tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu'),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=64, activation='relu'),
    tf.keras.layers.Dense(units=len(set(y)), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))
