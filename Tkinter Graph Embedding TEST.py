from tkinter import *
from pandas import *
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# incidentData = read_csv('airline-safety.csv')

matplotlib.style.use('dark_background')

tk = Tk()


def matplotCanvas(self):
    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    a.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])

    canvas = FigureCanvasTkAgg(f, self)
    canvas.show()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)


tk.mainloop()
