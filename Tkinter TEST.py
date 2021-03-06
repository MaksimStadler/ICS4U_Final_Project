from tkinter import *
from pandas import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

incidentData = read_csv('airline_incident_data.csv')

tk = Tk()


def addGraph():
    f = Figure(figsize=(5, 7), dpi=90)
    ax = f.add_subplot(111)

    ax.barh("airline", "avail_seat_km_per_week", data=incidentData)
    canvas = FigureCanvasTkAgg(f, tk)
    canvas.show()
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, sticky='nsew')

    tk.update_idletasks()
    if drop1.get() == 1:
        print(drop1.get())


tk.title('Airline Safety History')
tk.geometry('700x800')
tk.resizable(False, False)

drop1 = StringVar()
drop1.set(0)
drop2 = StringVar()
drop2.set(0)
drop3 = StringVar()
drop3.set(0)
drop4 = StringVar()
drop4.set(0)

airlineDropDown1 = OptionMenu(tk, drop1, 1, 2, 3, )
# airlineDropDown1.configure(height=1, width=30)
airlineDropDown1.grid(row=0, column=0, sticky='ew')
airlineDropDown2 = OptionMenu(tk, drop2, 1, 2, 3)
# airlineDropDown2.configure(height=1, width=30)
airlineDropDown2.grid(row=0, column=1, sticky='ew')

statisticButton1 = Button(text='Statistics', command=addGraph)
# statisticButton1.config(height=1)
statisticButton1.grid(row=1, columnspan=2, sticky='nsew')

label = Label(tk, text='TEXT')
# label.config(height=2, )
label.grid(row=2, columnspan=2, sticky='nsew')

airlineDropDown3 = OptionMenu(tk, drop3, 1, 2, 3)
# airlineDropDown3.configure(height=1, width=30)
airlineDropDown3.grid(row=4, column=0, sticky='ew')
airlineDropDown4 = OptionMenu(tk, drop4, 1, 2, 3)
# airlineDropDown3.configure(height=1, width=30)
airlineDropDown4.grid(row=4, column=1, sticky='ew')

statisticButton2 = Button(text='Statistics', command=addGraph)
# statisticButton2.config(height=1)
statisticButton2.grid(row=5, columnspan=2, sticky='nsew')

f = Figure(figsize=(5, 7), dpi=90)
ax = f.add_subplot(111)

ax.barh("airline", "avail_seat_km_per_week", data=incidentData)
canvas = FigureCanvasTkAgg(f, tk)
canvas.show()
canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, sticky='nsew')

tk.rowconfigure(0, weight=0)
tk.rowconfigure(1, weight=1)
tk.rowconfigure(2, weight=1)
tk.rowconfigure(3, weight=1)
tk.rowconfigure(4, weight=0)
tk.rowconfigure(5, weight=1)
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)

tk.mainloop()
print(drop1.get())
