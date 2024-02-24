from tkinter import Tk, Label, Entry, Button
from numpy import *
import matplotlib.pyplot as plt

class TkApp(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title('Графостроитель')
        self.geometry('400x400')
        self.configure(bg = '#c3e8e6', padx= 15, pady = 15)

        label = Label(self, text="Введите формулу:", font = "Arial 16 bold", pady = 10)
        label.pack()

        entry = Entry(self, font = 'Arial 12 bold')
        entry.pack(pady= 15)
        button = Button(self, text="Построить график", font = 'Arial 16 bold', command=lambda: self.plot_graph(entry.get()))
        button.pack()

    
    def plot_graph(self, formula):
        x = linspace(-10, 10, 100)
        y = eval(formula)
        fig = plt.figure(figsize=(6, 4), dpi=100)
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("График функции")
    
        def hover(self, event):
            if event.xdata is not None and event.ydata is not None:
                ax = plt.gca()
                ax.format_coord = lambda x, y: "x={:.2f}, y={:.2f}".format(x, y)
                fig.canvas.draw()
        
        fig.canvas.mpl_connect("motion_notify_event", hover)
        plt.show()


App = TkApp()
App.mainloop()