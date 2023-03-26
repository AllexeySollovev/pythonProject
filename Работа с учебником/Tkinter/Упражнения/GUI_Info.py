from tkinter import *
class GUI:
    def __init__(self):
        self.window = Tk()

        self.labvar = StringVar()

        self.label = Label(self.window, textvariable=self.labvar)
        self.label.pack()

        self.bottom_frame = Frame(self.window)
        self.btn_info = Button(self.bottom_frame, text='Показать инфо', command=self.btnlabel)
        self.btn_exit = Button(self.bottom_frame, text='Выйти', command=self.window.destroy)

        self.btn_exit.pack(side='left')
        self.btn_info.pack(side='left')

        self.bottom_frame.pack()

        mainloop()

    def btnlabel(self):
        self.labvar.set('198320, Россия. Гатчинское шоссе.,\n'
                        'г.Санкт-Петербург,\n'
                        'Почта России')

if __name__ == '__main__':
    mygui = GUI()