from tkinter import *

tk = Tk()


class airlineWin():

    def __init__(self, *args, **kwargs):
        __init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='Start Page')
        label.grid(row=0, column=0)

        button1 = Button(self, text='Page 1')
        button1.bind(controller.show_frame(Page1))
        button1.grid(row=1, column=0)


class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='Page 1')
        label.grid(row=0, column=0)

        button2 = Button(self, text='Back')
        button2.bind(controller.show_frame(StartPage))
        button2.grid(row=1, column=0)


airlineWin()
tk.mainloop()
