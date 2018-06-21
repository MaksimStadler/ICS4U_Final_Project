from tkinter import *

tk = Tk()

tk.title('Airline Safety History')
tk.geometry('200x300')

drop1 = StringVar(tk)
drop1.set(0)
drop2 = StringVar(tk)
drop2.set(0)
drop3 = StringVar(tk)
drop3.set(0)
drop4 = StringVar(tk)
drop4.set(0)

airlineDropDown1 = OptionMenu(tk, drop1, 1, 2, 3)
# airlineDropDown1.configure(height=1, width=15)
airlineDropDown1.grid(row=0, column=0, sticky='ew')
airlineDropDown2 = OptionMenu(tk, drop2, 1, 2, 3)
# airlineDropDown2.configure(height=1, width=15)
airlineDropDown2.grid(row=0, column=1, sticky='ew')

statisticButton1 = Button(text='Statistics')
# statisticButton.config(height=2, width=56)
statisticButton1.grid(row=1, columnspan=2, sticky='nsew')

airlineDropDown3 = OptionMenu(tk, drop3, 1, 2, 3)
# airlineDropDown3.configure(height=1, width=15)
airlineDropDown3.grid(row=2, column=0, sticky='ew')
airlineDropDown4 = OptionMenu(tk, drop4, 1, 2, 3)
# airlineDropDown3.configure(height=1, width=15)
airlineDropDown4.grid(row=2, column=1, sticky='ew')

statisticButton2 = Button(text='Statistics')
# statisticButton.config(height=2, width=56)
statisticButton2.grid(row=3, columnspan=2, sticky='nsew')

tk.rowconfigure(0, weight=0)
tk.rowconfigure(1, weight=1)
tk.rowconfigure(2, weight=0)
tk.rowconfigure(3, weight=1)
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)

tk.mainloop()
