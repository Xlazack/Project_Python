import tkinter as tk
from tkinter import filedialog

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
from functions import loadFiles
from functions import createNN
from functions import useModel
from functions import inspectLoadedFile
from evenNewerDatasetCutter import datasetCutter
import os
import shutil
from keras.models import load_model




class CSVPlotter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Plotter")

        self.filepath = ""
        self.data = None

        self.prepare_nn_btn = tk.Button(self, text="PRZYGOTUJ SIEC NEURONOWA", command=self.prepare_neural_network)
        self.prepare_nn_btn.pack()

        self.choose_file_btn = tk.Button(self, text="WGRAJ PLIK W FORMACIE .csv", command=self.choose_file)
        self.choose_file_btn.pack()

        self.plot_btn = tk.Button(self, text="GENERUJ WYKRES", command=self.plot)
        self.plot_btn.pack()

        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.upload_full_file_btn = tk.Button(self, text="Wczytaj pelny plik", command=self.upload_full_file)
        self.upload_full_file_btn.pack()

        self.check_full_file_btn = tk.Button(self, text="Sprawdz pelny plik", command=self.check_full_file)
        self.check_full_file_btn.pack()

        self.show_full_file_btn = tk.Button(self, text="Pokaz podzielony plik", command=self.show_full_file)
        self.show_full_file_btn.pack()


    def prepare_neural_network(self):
        loadFiles()
        createNN()
    def upload_full_file(self):
        self.otherFilepath = filedialog.askopenfilename()
        datasetCutter(self.otherFilepath)

    def check_full_file(self):
        if os.path.exists('neural_network.h5'):
            self.model = load_model('neural_network.h5')
        global data
        data = inspectLoadedFile("./dir")
    def choose_file(self):
        self.filepath = filedialog.askopenfilename()

    def show_full_file(self):
        for index,category in data:
            if  category == 1:
                image_path = "Zgiecie_nadgarstka.jpg"
            elif category == 2:
                image_path = "Wyprost_nadgarstka.jpg"
            elif category == 3:
                image_path = "Zgiecie_lokcia.jpg"
            elif category == 4:
                image_path = "Wyprost_lokcia.jpg"
            elif category == 5:
                image_path = "combo13.jpg"
            elif category == 6:
                image_path = "combo14.jpg"
            elif category == 7:
                image_path = "combo23.jpg"
            elif category == 8:
                image_path = "combo24.jpg"
            else : print ("error")
            image = Image.open(image_path)
            image.thumbnail((200, 200))  # Adjust the size of the thumbnail as needed
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo
    def plot(self):
        if self.filepath:
            self.data = pd.read_csv(self.filepath, delimiter=";", decimal=",", header=None)
            self.data = self.data.drop(0).astype('float32')

            fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

            axs[0, 0].plot(self.data.iloc[:, 0], self.data.iloc[:, 1])
            axs[0, 0].set_title("ZGINACZ NADGARSTKA OD CZASU")
            axs[0, 0].set_xlabel("CZAS [sec.]")
            axs[0, 0].set_ylabel("ZGINACZ NADGARSTKA [%]")

            axs[0, 1].plot(self.data.iloc[:, 0], self.data.iloc[:, 2])
            axs[0, 1].set_title("BICEPS OD CZASU")
            axs[0, 1].set_xlabel("CZAS [sec.]")
            axs[0, 1].set_ylabel("BICEPS [%]")

            axs[1, 0].plot(self.data.iloc[:, 0], self.data.iloc[:, 3])
            axs[1, 0].set_title("PROSTOWNIK NADGARSTKA OD CZASU")
            axs[1, 0].set_xlabel("CZAS [sec.]")
            axs[1, 0].set_ylabel("PROSTOWNIK NADGARSTKA [%]")

            axs[1, 1].plot(self.data.iloc[:, 0], self.data.iloc[:, 4])
            axs[1, 1].set_title("TRICEPS OD CZASU")
            axs[1, 1].set_xlabel("CZAS [sec.]")
            axs[1, 1].set_ylabel("TRICEPS [%]")

            fig.tight_layout()

            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().pack()

            # Load and display image
            x = useModel(self.filepath)
            print (x)
            if  x == 1:
                image_path = "Zgiecie_nadgarstka.jpg"
            elif x == 2:
                image_path = "Wyprost_nadgarstka.jpg"
            elif x == 3:
                image_path = "Zgiecie_lokcia.jpg"
            elif x == 4:
                image_path = "Wyprost_lokcia.jpg"
            elif x == 5:
                image_path = "combo13.jpg"
            elif x == 6:
                image_path = "combo14.jpg"
            elif x == 7:
                image_path = "combo23.jpg"
            elif x == 8:
                image_path = "combo24.jpg"
            else : print ("error")
            image = Image.open(image_path)
            image.thumbnail((200, 200))  # Adjust the size of the thumbnail as needed
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo



if __name__ == "__main__":
    app = CSVPlotter()
    app.iconbitmap("ikona_emg.ico")
    app.mainloop()
