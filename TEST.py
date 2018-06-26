from tkinter import *

tk = Tk()

from ttkthemes import ThemedStyle

app = tk(useTtk=True)
app.ttkStyle = ThemedStyle(app.topLevel)
app.ttkStyle.set_theme("plastik")
