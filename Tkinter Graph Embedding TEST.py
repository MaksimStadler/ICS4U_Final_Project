from tkinter import *
from pandas import *
import matplotlib
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

incidentData = read_csv('airline-safety.csv')

matplotlib.style.use('dark_background')

incidentPlot = sb.lmplot(x='incidents_85_99', y='avail_seat_km_per_week', data=incidentData)
# plt.show()
tk = Tk()

tk.title('TEST')

statisticButton = Button(text='Statistics')
# statisticButton.config(height=2, width=56)
# statisticButton.bind(canvasPlot)
statisticButton.grid(columnspan=3, sticky='nsew')

# def canvasPlot():
# f = Figure(figsize=(3, 3), dpi=100)
# a = f.add_subplot(111)
# a.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])
canvas = FigureCanvasTkAgg(incidentPlot, tk)
canvas.show()
canvas.get_tk_widget().grid(row=0, column=0)

tk.mainloop()
