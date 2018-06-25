from pandas import *
from tkinter import *

tk = Tk()

rankData = read_csv('airline_rank_data.csv').drop(columns=['airline', 'In top 100-2015?'])

graphVariableList = ['Seat Kilometers Per Week', 'Incidents from 2000 - 2014',
                     'Accidents From 2001 - 2014', 'Fatalities from 2000 - 2014', 'Rank']

rankDataColumns = list(rankData)

graphDropOption1 = StringVar(tk)
graphDropOption1.set('Seat Kilometers Per Week')

# option1 = rankDataColumns[graphVariableList.index(graphDropOption1)]

print(graphDropOption1)
