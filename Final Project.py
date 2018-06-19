# import data, graphing, and tkinter libraries
from tkinter import *
from pandas import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# read, sort, and distribute dataset into variables
airData = read_csv('airline-safety.csv')

airlines = airData['airline'].tolist()


def percentDecrease(incidents_85_99, incidents_00_14):
    pd = abs(incidents_85_99 - incidents_00_14) / incidents_85_99
    return pd


def incidentRate(airline, fatalities_00_14):
    rate = fatalities_00_14 / 14
    return ('from 2001 to 2014, there were {} fatalities per year on {}.').format(rate, airline)


print(airData['airline'].loc[0])
