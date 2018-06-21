from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

tk = Tk()


def addGraph():
    f = Figure(figsize=(3, 3), dpi=100)
    a = f.add_subplot(111)
    a.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])
    canvas = FigureCanvasTkAgg(f, tk)
    canvas.show()
    canvas.get_tk_widget().grid(row=2, column=0)

    tk.update_idletasks()


B = Button(tk, text="Change graph", command=addGraph)

B.grid(row=0, column=1)

f = Figure(figsize=(3, 3), dpi=100)
a = f.add_subplot(111)
a.plot([1, 2, 3, 4], [1, 2, 3, 4])
canvas = FigureCanvasTkAgg(f, tk)
canvas.show()
canvas.get_tk_widget().grid(row=2, column=0)

tk.mainloop()
