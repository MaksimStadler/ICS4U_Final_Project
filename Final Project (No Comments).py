# import data, graphing, and tkinter libraries
from tkinter import *
from pandas import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use('dark_background')

# read, sort, and distribute dataset into variables
# incidentData = read_csv('''https://raw.githubusercontent.com/
# datasets/five-thirty-eight-datasets/master/
# datasets/airline-safety/data/airline-safety.csv''')
# rankData = read_csv('https://query.data.world/s/tahtclz4hjwzg352jllsbgwtafht2u')
incidentData = read_csv('airline_incident_data.csv')
rankData = read_csv('airline_rank_data.csv').drop(columns=['airline', 'In top 100-2015?'])

airlineList = incidentData['airline'].tolist()

functionDropList = ['Percentage Decrease In Incidents', 'Percentage Decrease In Accidents',
                    'Percentage Decrease In Fatalities', 'Fatalities Per Year',
                    'Accident Fatality Rate']

graphVariableList = ['Seat Kilometers Per Week', 'Incidents from 2000 - 2014',
                     'Accidents From 2001 - 2014', 'Fatalities from 2000 - 2014', 'Rank']

rankDataColumns = list(rankData)


def incidentDecrease(airline, incidents_85_99, incidents_00_14):
    if incidents_85_99 != 0:
        percent = 100 * ((incidents_85_99 - incidents_00_14) / incidents_85_99)
    else:
        percent = 0
    return '''
    On {}, there were {:.0f}% less incidents between 2000 and 2014 than there were between 1985 and 1999.' \
    '''.format(airline, percent)


def accidentDecrease(airline, accidents_85_99, accidents_00_14):
    if accidents_85_99 != 0:
        percent = 100 * ((accidents_85_99 - accidents_00_14) / accidents_85_99)
    else:
        percent = 0
    return '''
    On {}, there were {:.0f}% less accidents between 2000 and 2014 than there were between 1985 and 1999.
    '''.format(airline, percent)


def fatalityDecrease(airline, fatalities_85_99, fatalities_00_14):
    if fatalities_85_99 != 0:
        percent = 100 * ((fatalities_85_99 - fatalities_00_14) / fatalities_85_99)
    else:
        percent = 0
    return '''
    On {}, there were {:.0f}% less fatalities between 2000 and 2014 than there were between 1985 and 1999.
    '''.format(airline, percent)


def deathsPerYear(airline, fatalities):
    rate = fatalities / 15
    return 'From 2000 to 2014, there were approximately {:.0f} fatalities per year on {}.'.format(rate, airline)


def deathsPerAccident(airline, fatal_accidents_00_14, fatalities):
    if fatalities != 0:
        average = fatalities / fatal_accidents_00_14
    else:
        average = 0
    return 'From 2000 to 2014, every {} accident killed {:.0f} people on average.'.format(airline, average)


tk = Tk()

tk.title('Airline Statistics')
tk.iconbitmap(default='icon.ico')
tk.geometry('700x700')
tk.resizable(False, False)

tk.rowconfigure(0, weight=0)
tk.rowconfigure(1, weight=1)
tk.rowconfigure(2, weight=1)
tk.rowconfigure(3, weight=1)
tk.rowconfigure(4, weight=0)
tk.rowconfigure(5, weight=1)
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)

airlineDropOption = StringVar(tk)
airlineDropOption.set('Choose an airline')
functionDropOption = StringVar(tk)
functionDropOption.set('Choose a statistic')
graphDropOption1 = StringVar(tk)
graphDropOption1.set('Choose a variable')
graphDropOption2 = StringVar(tk)
graphDropOption2.set('Choose another variable')

airlineDropDown = OptionMenu(tk, airlineDropOption, *airlineList)
airlineDropDown.configure(height=1, width=30)
airlineDropDown.grid(row=0, column=0, sticky='ew')
functionDropDown = OptionMenu(tk, functionDropOption, *functionDropList)
functionDropDown.configure(height=1, width=30)
functionDropDown.grid(row=0, column=1, sticky='ew')
graphDropDown1 = OptionMenu(tk, graphDropOption1, *graphVariableList)
graphDropDown1.configure(height=1, width=30)
graphDropDown1.grid(row=4, column=0, sticky='ew')
graphDropDown2 = OptionMenu(tk, graphDropOption2, *graphVariableList)
graphDropDown2.configure(height=1, width=30)
graphDropDown2.grid(row=4, column=1, sticky='ew')

statisticLabel = Label(tk, text='(Statistics)')
statisticLabel.grid(row=2, columnspan=2, sticky='nsew')

f = Figure(dpi=100)
ax = f.add_subplot(111)
ax.barh("airline", "avail_seat_km_per_week", data=incidentData)
ax.set_xlabel('Seat Kilometers Per Week (Biilions)')
ax.set_ylabel('Airlines')
ax.yaxis.set_tick_params(labelsize=5)
ax.xaxis.set_tick_params(labelsize=7)
ax.get_xaxis().get_major_formatter().set_scientific(False)
canvas = FigureCanvasTkAgg(f, tk)
canvas.draw()
canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, sticky='nsew')


def userPlotFunc():
    if graphDropOption1.get() != 'Choose a variable' and graphDropOption2.get() != 'Choose another variable':
        option1 = rankDataColumns[graphVariableList.index(graphDropOption1.get())]
        option2 = rankDataColumns[graphVariableList.index(graphDropOption2.get())]

        f = Figure(figsize=(5, 5), dpi=100)
        ax = f.add_subplot(111)

        ax.scatter(option1, option2, data=rankData)
        ax.set_xlabel(graphDropOption1.get())
        ax.set_ylabel(graphDropOption2.get())
        ax.yaxis.set_tick_params(labelsize=7)
        ax.xaxis.set_tick_params(labelsize=7)
        canvas = FigureCanvasTkAgg(f, tk)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, sticky='nsew')

        tk.update_idletasks()


def statisticCall():
    if functionDropOption.get() == 'Percentage Decrease In Incidents':
        statisticLabel.config(text=incidentDecrease(airlineDropOption.get(),
                                                    incidentData['incidents_85_99'].iloc[
                                                        airlineList.index(airlineDropOption.get())],
                                                    incidentData['incidents_00_14'].iloc[
                                                        airlineList.index(airlineDropOption.get())]))
    elif functionDropOption.get() == 'Percentage Decrease In Accidents':
        statisticLabel.config(text=accidentDecrease(airlineDropOption.get(),
                                                    incidentData['fatal_accidents_85_99'].iloc[
                                                        airlineList.index(airlineDropOption.get())],
                                                    incidentData['fatal_accidents_00_14'].iloc[
                                                        airlineList.index(airlineDropOption.get())]))
    elif functionDropOption.get() == 'Percentage Decrease In Fatalities':
        statisticLabel.config(text=fatalityDecrease(airlineDropOption.get(),
                                                    incidentData['fatalities_85_99'].iloc[
                                                        airlineList.index(airlineDropOption.get())],
                                                    incidentData['fatalities_00_14'].iloc[
                                                        airlineList.index(airlineDropOption.get())]))
    elif functionDropOption.get() == 'Fatalities Per Year':
        statisticLabel.config(text=deathsPerYear(airlineDropOption.get(),
                                                 incidentData['fatalities_00_14'].iloc[
                                                     airlineList.index(airlineDropOption.get())]))
    elif functionDropOption.get() == 'Accident Fatality Rate':
        statisticLabel.config(text=deathsPerAccident(airlineDropOption.get(),
                                                     incidentData['fatal_accidents_00_14'].iloc[
                                                         airlineList.index(airlineDropOption.get())],
                                                     incidentData['fatalities_00_14'].iloc[
                                                         airlineList.index(airlineDropOption.get())]))
    tk.update_idletasks()


statisticButton1 = Button(text='Statistics', command=statisticCall)
statisticButton1.config(height=2)
statisticButton1.grid(row=1, columnspan=2, sticky='nsew')

statisticButton2 = Button(text='Statistics', command=userPlotFunc)
statisticButton2.config(height=2)
statisticButton2.grid(row=5, columnspan=2, sticky='nsew')

tk.mainloop()
