from tkinter import *
from pandas import *
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

incidentData = read_csv('airline-safety.csv')

tk = Tk()



tk.mainloop()