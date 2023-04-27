"""import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

    def choose_file(self):
        self.filepath = filedialog.askopenfilename()

    def plot(self):
        if self.filepath:
            self.data = pd.read_csv(self.filepath)

            fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

            axs[0, 0].plot(self.data.iloc[:, 0], self.data.iloc[:, 1])
            axs[0, 0].set_title("ZGINACZ NADGARSTKA OD CZASU")

            axs[0, 1].plot(self.data.iloc[:, 0], self.data.iloc[:, 2])
            axs[0, 1].set_title("BICEPS OD CZASU")

            axs[1, 0].plot(self.data.iloc[:, 0], self.data.iloc[:, 3])
            axs[1, 0].set_title("PROSTOWNIK NADGARSTKA OD CZASU")

            axs[1, 1].plot(self.data.iloc[:, 0], self.data.iloc[:, 4])
            axs[1, 1].set_title("TRICEPS OD CZASU")

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.draw()
            canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVPlotter(master=root)
    app.mainloop()
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

    def choose_file(self):
        self.filepath = filedialog.askopenfilename()

    def plot(self):
        if self.filepath:
            self.data = pd.read_csv(self.filepath)

            fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

            axs[0, 0].plot(self.data.iloc[:, 0], self.data.iloc[:, 1])
            axs[0, 0].set_title("ZGINACZ NADGARSTKA OD CZASU")

            axs[0, 1].plot(self.data.iloc[:, 0], self.data.iloc[:, 2])
            axs[0, 1].set_title("BICEPS OD CZASU")

            axs[1, 0].plot(self.data.iloc[:, 0], self.data.iloc[:, 3])
            axs[1, 0].set_title("PROSTOWNIK NADGARSTKA OD CZASU")

            axs[1, 1].plot(self.data.iloc[:, 0], self.data.iloc[:, 4])
            axs[1, 1].set_title("TRICEPS OD CZASU")

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVPlotter(master=root)
    app.mainloop()
