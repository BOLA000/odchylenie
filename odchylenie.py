import tkinter as tk
from math import sqrt

class OdchylenieStandardowe(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label_wartoscs = tk.Label(self, text="Wpisz liczby oddzielone przecinkiem:")
        self.label_wartoscs.pack()

        self.entry_wartoscs = tk.Entry(self)
        self.entry_wartoscs.pack()

        self.button_calculate = tk.Button(self, text="Oblicz odchylenie standardowe", command=self.odchyleniestandardowe)
        self.button_calculate.pack()

        self.label_result = tk.Label(self, text="Odchylenie standardowe: ")
        self.label_result.pack()

        self.entry_result = tk.Entry(self)
        self.entry_result.pack()

    def odchyleniestandardowe(self):
       
        wartoscistring = self.entry_wartoscs.get()

        try:
            wartosci = [float(wartosc) for wartosc in wartoscistring.split(", " and ",")]
        except ValueError:
            self.entry_result.delete(0, tk.END)
            self.entry_result.insert(0, "Liczby mają być oddzielone przecinkiem")
            return

        mean = sum(wartosci) / len(wartosci)

        wzor = sum((wartosc - mean)**2 for wartosc in wartosci) / len(wartosci)

        odchyleniestand = sqrt(wzor)

        self.entry_result.delete(0, tk.END)
        self.entry_result.insert(0, f"{odchyleniestand}")

if __name__ == "__main__":
    wlacz = tk.Tk()
    program = OdchylenieStandardowe(wlacz)
    program.pack()
    wlacz.mainloop()