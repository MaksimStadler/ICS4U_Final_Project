# import data, graphing, and tkinter libraries
from tkinter import *
from pandas import *
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# read, sort, and distribute dataset into variables
incidentData = read_csv('airline-safety.csv')

airlines = incidentData['airline'].tolist()


def percentDecrease(incidents_85_99, incidents_00_14):
    pd = abs(incidents_85_99 - incidents_00_14) / incidents_85_99
    return pd


print(incidentData['airline'].loc)
