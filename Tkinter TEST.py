from tkinter import *
from pandas import *
import matplotlib
import seaborn as sb

# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# def canvasPlot():
#     f = Figure(figsize=(3, 3), dpi=100)
#     a = f.add_subplot(111)
#     a.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])
#     canvas = FigureCanvasTkAgg(f, tk)
#     canvas.show()
#     canvas.get_tk_widget().grid(row=0, column=3)
#     tk.update()

# matplotlib.style.use('dark_background')
#
# incidentData = read_csv('airline-safety.csv')
#
# incidentPlot = sb.lmplot(x='airline', y='avail_seat_km_per_week', data=incidentData)


# def canvasPlot():
#     plt.show()


tk = Tk()

tk.title('Airline Safety History')
tk.geometry('400x70')

x = StringVar(tk)
x.set(0)

airlineDropDown1 = OptionMenu(tk, x, 1, 2, 3)
# airlineDropDown1.configure(height=1, width=15)
airlineDropDown1.grid(row=0, column=0, sticky='ew')
airlineDropDown2 = OptionMenu(tk, x, 1, 2, 3)
# airlineDropDown2.configure(height=1, width=15)
airlineDropDown2.grid(row=0, column=1, sticky='ew')
airlineDropDown3 = OptionMenu(tk, x, 1, 2, 3)
# airlineDropDown3.configure(height=1, width=15)
airlineDropDown3.grid(row=0, column=2, sticky='ew')

statisticButton = Button(text='Statistics')
# statisticButton.config(height=2, width=56)
# statisticButton.bind(canvasPlot)
statisticButton.grid(columnspan=3, sticky='nsew')

tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)
tk.columnconfigure(2, weight=1)
tk.rowconfigure(0, weight=0)
tk.rowconfigure(1, weight=1)

tk.mainloop()
