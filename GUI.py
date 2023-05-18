import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class CSVPlotter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("CSV Plotter")
        self.pack()

        self.filepath = ""
        self.data = None

        # create widgets
        self.choose_file_btn = tk.Button(self, text="WGRAJ PLIK W FORMACIE .csv", command=self.choose_file)
        self.choose_file_btn.pack()

        self.plot_btn = tk.Button(self, text="GENERUJ WYKRES", command=self.plot)
        self.plot_btn.pack()

        self.image_label = tk.Label(self)
        self.image_label.pack()

    def choose_file(self):
        self.filepath = filedialog.askopenfilename()

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

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.get_tk_widget().pack()

            # Load and display image
            image_path = "Zgiecie_lokiec.jpg"  # Replace with the actual image file path
            image = Image.open(image_path)
            image.thumbnail((300, 300))  # Adjust the size of the thumbnail as needed
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

            plt.show()
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVPlotter(master=root)
    app.mainloop()