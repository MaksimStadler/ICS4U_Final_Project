import tkinter

root = Tk()

panel = Label(root, image='208.jpg')
panel.pack(side="bottom", fill="both", expand="yes")


def imageUpdate():
    panel.configure(image=img2)
    panel.image = img2


root.bind("<Return>", callback)
root.mainloop()
