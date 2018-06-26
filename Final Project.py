# import pandas, tkinter, and various matplotlib libraries
from tkinter import *
from pandas import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Graph theme is set to dark for A S T H E T I C
plt.style.use('dark_background')

# read in data files from local storage
incidentData = read_csv('airline_incident_data.csv')
rankData = read_csv('airline_rank_data.csv').drop(columns=['airline', 'In top 100-2015?'])

# read in data files from web URL (optional)
# incidentData = read_csv('''https://raw.githubusercontent.com/
# datasets/five-thirty-eight-datasets/master/
# datasets/airline-safety/data/airline-safety.csv''')
#
# # airline and top 100 columns are dropped from rankdata to simplify indexing later
# rankData = read_csv('https://query.data.world/s/tahtclz4hjwzg352jllsbgwtafht2u').drop(
#     columns=['airline', 'In top 100-2015?'])

# convert airline column to a list for later use in dropdown
airlineList = incidentData['airline'].tolist()

# dropdown list for functions is declared
functionDropList = ['Percentage Decrease In Incidents', 'Percentage Decrease In Accidents',
                    'Percentage Decrease In Fatalities', 'Fatalities Per Year',
                    'Accident Fatality Rate']

# dropdown list for graphing variables is declared
graphVariableList = ['Seat Kilometers Per Week', 'Incidents from 2000 - 2014',
                     'Accidents From 2001 - 2014', 'Fatalities from 2000 - 2014', 'Rank']

# column headers in rankData are placed into a list
rankDataColumns = list(rankData)


# functions for upper portion of window are defined and all output is formatted as a standalone scentence
# all output is rounded to a whole number

# the incient totals of one airline from 2 time periods are used in a percentage decrease calculation
def incidentDecrease(airline, incidents_85_99, incidents_00_14):
    if incidents_85_99 != 0:
        percent = 100 * ((incidents_85_99 - incidents_00_14) / incidents_85_99)
    else:
        percent = 0
    return '''
    On {}, there were {:.0f}% less incidents between 2000 and 2014 than there were between 1985 and 1999.' \
    '''.format(airline, percent)


# the accient totals of one airline from 2 time periods are used in a percentage decrease calculation
def accidentDecrease(airline, accidents_85_99, accidents_00_14):
    if accidents_85_99 != 0:
        percent = 100 * ((accidents_85_99 - accidents_00_14) / accidents_85_99)
    else:
        percent = 0
    return '''
    On {}, there were {:.0f}% less accidents between 2000 and 2014 than there were between 1985 and 1999.
    '''.format(airline, percent)


# the fatality totals of one airline from 2 time periods are used in a percentage decrease calculation
def fatalityDecrease(airline, fatalities_85_99, fatalities_00_14):
    if fatalities_85_99 != 0:
        percent = 100 * ((fatalities_85_99 - fatalities_00_14) / fatalities_85_99)
    else:
        percent = 0
    return '''
    On {}, there were {:.0f}% less fatalities between 2000 and 2014 than there were between 1985 and 1999.
    '''.format(airline, percent)


# the total amount of fatalities of one airline is divided by the number of years in the 2000 - 2015 time period
def deathsPerYear(airline, fatalities):
    rate = fatalities / 15
    return 'From 2000 to 2014, there were approximately {:.0f} fatalities per year on {}.'.format(rate, airline)


# the total amount of fatalities is divided by the total amount of accidents
def deathsPerAccident(airline, fatal_accidents_00_14, fatalities):
    if fatalities != 0:
        average = fatalities / fatal_accidents_00_14
    else:
        average = 0
    return 'From 2000 to 2014, every {} accident killed {:.0f} people on average.'.format(airline, average)


# the Tk() function is redeclared for simplicity
tk = Tk()

# window title, size, icon, and resizability properties are set
tk.title('Airline Statistics')
tk.iconbitmap(default='icon.ico')
tk.geometry('700x700')
tk.resizable(False, False)

# the rate at which columns/rows expand can be set if the windows is resizable
tk.rowconfigure(0, weight=0)
tk.rowconfigure(1, weight=1)
tk.rowconfigure(2, weight=1)
tk.rowconfigure(3, weight=1)
tk.rowconfigure(4, weight=0)
tk.rowconfigure(5, weight=1)
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)

# all dropdown vaviables are initialized and temporary strings are appended for display purposes
airlineDropOption = StringVar(tk)
airlineDropOption.set('Choose an airline')
functionDropOption = StringVar(tk)
functionDropOption.set('Choose a statistic')
graphDropOption1 = StringVar(tk)
graphDropOption1.set('Choose an X variable')
graphDropOption2 = StringVar(tk)
graphDropOption2.set('Choose a Y variable')

# dropdown menus are created using the airline, function, and graph variable lists created above,
# they are also tied to the appropriate variables
# they are also arranged using the tkinter grid layout
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

# a label is created to show the statistics rather than them being printed because this is a windows based program
statisticLabel = Label(tk, text='(Statistics)')
statisticLabel.grid(row=2, columnspan=2, sticky='nsew')

# a figure is created and a temporary graph is appended to it
f = Figure(dpi=100)
ax = f.add_subplot(111)

# a temporary horizontal bar graph is created to show the seat kilometers per week on every airline in rankData
ax.barh("airline", "avail_seat_km_per_week", data=incidentData)
# x and y axis labels are set
ax.set_xlabel('Seat Kilometers Per Week (Billions)')
ax.set_ylabel('Airlines')
# tick number fonts are changed because the defaults are too large
ax.yaxis.set_tick_params(labelsize=5)
ax.xaxis.set_tick_params(labelsize=7)
# this function disables the text that tells you the x axis numbers are in billions because it is ugly and confusing
ax.get_xaxis().get_major_formatter().set_scientific(False)
# the canvas containing the graph is placed within the window like a good boy
canvas = FigureCanvasTkAgg(f, tk)
canvas.draw()
canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, sticky='nsew')


# userPlotFunc() uses no arguments because it created a paradox that made me feel sad
# instead, the function calls the graph variables all by itself and uses them as x and y variables for a scatter plot
def userPlotFunc():
    if graphDropOption1.get() != 'Choose a variable' and graphDropOption2.get() != 'Choose another variable':
        # the index of the dropdown variable list is used to call the column name from the rankData dataframe
        option1 = rankDataColumns[graphVariableList.index(graphDropOption1.get())]
        option2 = rankDataColumns[graphVariableList.index(graphDropOption2.get())]

        # a new figure is created on top of the last one instead of replacing it
        # because it wasn't working and it was making me sad again
        f = Figure(figsize=(5, 5), dpi=100)
        ax = f.add_subplot(111)

        # a scatter plot is created based on the current selections in the bottom 2 dropdown menus
        ax.scatter(option1, option2, data=rankData)
        ax.set_xlabel(graphDropOption1.get())
        ax.set_ylabel(graphDropOption2.get())
        ax.yaxis.set_tick_params(labelsize=7)
        ax.xaxis.set_tick_params(labelsize=7)
        canvas = FigureCanvasTkAgg(f, tk)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, sticky='nsew')

        # we need to manually update the tkinter window by slapping mainloop() in the face with update_idletasks()
        # because it won't listen unless we do that
        tk.update_idletasks()


# statisticCall() checks the current selection of functionDropDown and calls the corresponding function
# it also fills in the arguments with the appropriate variables from airlineList and functionDropList
# once again ,teh index of hte airlineDropOption variable is used to call the proper culunm label from incidentData
# each function call sets the returned text as the statisticLabel text
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
    # just need to slap mainloop() is the face again so we can update the label
    tk.update_idletasks()


# this statistic button calls statisticCall() and relies on the upper dropdown lists for vaiables
statisticButton1 = Button(text='Statistics', command=statisticCall)
statisticButton1.config(height=2)
statisticButton1.grid(row=1, columnspan=2, sticky='nsew')

# this statistic button calls userPlotFunc() and relies on the lower dropdown lists for vaiables
statisticButton2 = Button(text='Statistics', command=userPlotFunc)
statisticButton2.config(height=2)
statisticButton2.grid(row=5, columnspan=2, sticky='nsew')

# as neglective as mainloop may be, we still need to call it so the tkinter windows doesn't instantaneously close when
# it opens causing us to question our vision and/or sanity
tk.mainloop()
