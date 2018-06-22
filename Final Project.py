# import data, graphing, and tkinter libraries
from tkinter import *
from pandas import *
import matplotlib
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# read, sort, and distribute dataset into variables
airData = read_csv('airline-safety.csv')
incidentData = read_csv('accident_details.txt', sep=' | ')

airlineList = airData['airline'].tolist()

tk = Tk()


def percentDecrease(incidents_85_99, incidents_00_14):
    pd = abs(incidents_85_99 - incidents_00_14) / incidents_85_99
    return pd


def incidentRate(airline, fatalities):
    rate = fatalities / 14
    return 'from 2001 to 2014, there were {} fatalities per year on {}.'.format(rate, airline)


def userPlotFunc(option1, option2):
    userPlot = sb.lmplot(x=option1, y=option2, data=airData)
    canvas = FigureCanvasTkAgg(userPlot, tk)
    canvas.show()
    canvas.get_tk_widget().grid(row=2, column=0)

    tk.update_idletasks()


print(incidentData.loc[22])
