# import data, graphing, and tkinter libraries
from tkinter import *
from pandas import *

# read, sort, and distribute dataset into variables
incidentData = read_csv(
    'https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

airlines = incidentData['airline'].tolist()

# set tkinter widgets and properties
tk = Tk()

tk.title('Airline Safety History')
tk.geometry('300x100')

airlineDropVar = StringVar(tk)
airlineDropVar.set(airlines[0])

airlineDropDown1 = OptionMenu(tk, airlineDropVar, *airlines).grid(row=0, column=0, sticky=W)
airlineDropDown2 = OptionMenu(tk, airlineDropVar, *airlines).grid(row=0, column=1, sticky=W)
airlineDropDown3 = OptionMenu(tk, airlineDropVar, *airlines).grid(row=0, column=2, sticky=W)
statisticButton = Button(text='Statistics').grid(row=1, columnspan=3)

tk.mainloop()
