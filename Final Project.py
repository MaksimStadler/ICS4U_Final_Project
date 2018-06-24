# import data, graphing, and tkinter libraries
from tkinter import *
from pandas import *
import seaborn as sb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# read, sort, and distribute dataset into variables
# incidentData = read_csv('''https://raw.githubusercontent.com/
# datasets/five-thirty-eight-datasets/master/
# datasets/airline-safety/data/airline-safety.csv''')
# rankData = read_csv('https://query.data.world/s/tahtclz4hjwzg352jllsbgwtafht2u')
incidentData = read_csv('airline_incident_data.csv')
rankData = read_csv('airline_rank_data.csv')

airlineList1 = incidentData['airline'].tolist()
airlineList2 = rankData['airline'].tolist()

functionDropList = ['Percentage Decrease In Incidents', 'Percentage Decrease In Accidents',
                    'Percentage Decrease In Fatalities', 'Fatalities Per Year',
                    'Accident Fatality Rate']


def incidentDecrease(airline, incidents_85_99, incidents_00_14):
    percent = 100 * abs(incidents_85_99 - incidents_00_14) / incidents_85_99
    return '''
    On {}, there were {:.0f}% less incidents between 2000 and 2014 than there were between 1985 and 1999.' \
    '''.format(airline, percent)


def accidentDecrease(airline, accidents_85_99, accidents_00_14):
    percent = 100 * abs(accidents_85_99 - accidents_00_14) / accidents_85_99
    return '''
    On {}, there were {:.0f}% less accidents between 2000 and 2014 than there were between 1985 and 1999.
    '''.format(airline, percent)


def fatalityDecrease(airline, fatalities_85_99, fatalities_00_14):
    percent = 100 * ((fatalities_85_99 - fatalities_00_14) / fatalities_85_99)
    return '''
    On {}, there were {:.0f}% less fatalities between 2000 and 2014 than there were between 1985 and 1999.
    '''.format(airline, percent)


def deathsPerYear(airline, fatalities):
    rate = fatalities / 15
    return 'From 2000 to 2014, there were approximately {:.0f} fatalities per year on {}.'.format(rate, airline)


def deathsPerAccident(airline, fatal_accidents_00_14, fatalities):
    average = fatalities / fatal_accidents_00_14
    return 'From 2000 to 2014, every {} accident killed {:.0f} people on average.'.format(airline, average)


tk = Tk()

tk.title('Airline Safety History')
tk.geometry('600x700')
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
graphDropOption2.set('Choose a variable to compare')

airlineDropDown = OptionMenu(tk, airlineDropOption, 1, 2, 3)
# airlineDropDown1.configure(height=1, width=30)
airlineDropDown.grid(row=0, column=0, sticky='ew')
functionDropDown = OptionMenu(tk, functionDropOption, 1, 2, 3)
# airlineDropDown2.configure(height=1, width=30)
functionDropDown.grid(row=0, column=1, sticky='ew')
graphDropDown1 = OptionMenu(tk, graphDropOption1, 1, 2, 3)
# airlineDropDown3.configure(height=1, width=30)
graphDropDown1.grid(row=4, column=0, sticky='ew')
graphDropDown2 = OptionMenu(tk, graphDropOption2, 1, 2, 3)
# airlineDropDown3.configure(height=1, width=30)
graphDropDown2.grid(row=4, column=1, sticky='ew')

statisticLabel = Label(tk, text='')
statisticLabel.grid(row=2, columnspan=2, sticky='nsew')


def userPlotFunc(option1, option2):
    userPlot = sb.lmplot(x=option1, y=option2, data=rankData)
    canvas = FigureCanvasTkAgg(userPlot, tk)
    canvas.show()
    canvas.get_tk_widget().grid(row=2, column=0)

    tk.update_idletasks()


def statisticCall():
    if functionDropOption == 'Percentage Decrease In Incidents':
        statisticLabel.config(incidentDecrease(airlineDropOption,
                                               incidentData['incidents_85_99'].iloc[
                                                   airlineList1.index(airlineDropOption)],
                                               incidentData['incidents_00_14'].iloc[
                                                   airlineList1.index(airlineDropOption)]))
    elif functionDropOption == 'Percentage Decrease In Accidents':
        statisticLabel.config(accidentDecrease(airlineDropOption,
                                               incidentData['fatal_accidents_85_99'].iloc[
                                                   airlineList1.index(airlineDropOption)],
                                               incidentData['fatal_accidents_00_14'].iloc[
                                                   airlineList1.index(airlineDropOption)]))
    elif functionDropOption == 'Percentage Decrease In Fatalities':
        statisticLabel.config(fatalityDecrease(airlineDropOption,
                                               incidentData['fatalities_85_99'].iloc[
                                                   airlineList1.index(airlineDropOption)],
                                               incidentData['fatalities_00_14'].iloc[
                                                   airlineList1.index(airlineDropOption)]))
    elif functionDropOption == 'Fatalities Per Year':
        statisticLabel.config(deathsPerYear(airlineDropOption, incidentData['fatalities_00_14'].iloc[
            airlineList1.index(airlineDropOption)]))
    elif functionDropOption == 'Accident Fatality Rate':
        statisticLabel.config(deathsPerAccident(airlineDropOption, incidentData['fatal_accidents_00_14'].iloc[
            airlineList1.index(airlineDropOption)], incidentData['fatalities_00_14'].iloc[
                                                    airlineList1.index(airlineDropOption)]))


statisticButton1 = Button(text='Statistics', command=statisticCall())
statisticButton1.config(height=2)
statisticButton1.grid(row=1, columnspan=2, sticky='nsew')

statisticButton2 = Button(text='Statistics', command=userPlotFunc(graphDropOption1, graphDropOption2))
statisticButton2.config(height=2)
statisticButton2.grid(row=5, columnspan=2, sticky='nsew')
