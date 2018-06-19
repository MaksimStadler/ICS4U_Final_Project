from tkinter import *

tk = Tk()

panel = Label(tk, image='208.jpg')
panel.grid(row=0, column=0)


def imageUpdate():
    panel.configure(image='209.jpg')
    panel.image = '209.jpg'


upButton = Button(tk, text='Update')
upButton.bind(imageUpdate)
upButton.grid(row=1, column=0)

tk.mainloop()
