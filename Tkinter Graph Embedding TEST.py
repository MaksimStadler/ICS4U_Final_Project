from tkinter import *
from pandas import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

incidentData = read_csv('airline-safety.csv')

tk = Tk()

# f = Figure(figsize=(10, 10), dpi=100)
# a = f.add_subplot(111)
# a.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])
#
# canvas = FigureCanvasTkAgg(f)
# canvas.show()
# canvas.get_tk_widget().pack(side='TOP', fill='BOTH', expand=True)

tk.mainloop()
