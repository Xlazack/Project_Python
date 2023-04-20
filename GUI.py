import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

# Funkcja rysująca wykres liniowy
def line_plot(x, y, xlabel, ylabel):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

sg.theme('DefaultNoMoreNagging')  # Ustawienie motywu

# Definicja layoutu okna
layout = [
    [sg.Text("Cześć, jestem programem badającym ruch przy pomocy analizy EMG!")],
    [sg.Text('Wybierz plik do wgrania w fomracie .csv:')],
    [sg.Input(), sg.FileBrowse()],
    [sg.Button('Wgraj'), sg.Button('Anuluj')],
]

window = sg.Window('ANALIZA EMG', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Anuluj':
        break
    if event == 'Wgraj':
        filename = values[0]
        try:
            df = pd.read_csv(filename)
        except:
            sg.popup_error('Błąd odczytu pliku')
            continue
        sg.popup('Plik został wczytany', f'Liczba wierszy: {len(df)}', title='PLIK WGRANY PRAWIDŁOWO')

        # Rysowanie wykresów
        plt.close('all')
        fig1, ax1 = plt.subplots()
        line_plot(df['a'], df['b'], 'a', 'b')
        fig2, ax2 = plt.subplots()
        line_plot(df['a'], df['c'], 'a', 'c')
        fig3, ax3 = plt.subplots()
        line_plot(df['a'], df['d'], 'a', 'd')
        fig4, ax4 = plt.subplots()
        line_plot(df['a'], df['e'], 'a', 'e')

        plt.plot(df['A'], df['B'])
        plt.xlabel('A')
        plt.ylabel('B')
        plt.title('Wykres liniowy kolumny B od kolumny A')
        plt.show()

        # Wyświetlenie okien z wykresami
        sg.popup('Wykres kolumny b od a', title='Wykres 1', location=(0, 0), keep_on_top=True)
        plt.show(block=False, fig=fig1)
        sg.popup('Wykres kolumny c od a', title='Wykres 2', location=(0, 100), keep_on_top=True)
        plt.show(block=False, fig=fig2)
        sg.popup('Wykres kolumny d od a', title='Wykres 3', location=(0, 200), keep_on_top=True)
        plt.show(block=False, fig=fig3)
        sg.popup('Wykres kolumny e od a', title='Wykres 4', location=(0, 300), keep_on_top=True)
        plt.show(block=False, fig=fig4)

window.close()

