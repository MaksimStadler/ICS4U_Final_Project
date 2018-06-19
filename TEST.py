# import data, graphing, and tkinter libraries
from tkinter import *
from pandas import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# read, sort, and distribute dataset into variables
airData = read_csv('airline-safety.csv')

var = airData.loc[0]

print(var)
