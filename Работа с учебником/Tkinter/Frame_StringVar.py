from tkinter.messagebox import *
from tkinter import *
class MyGUI():
    def __init__(self):
        self.window = Tk()
        self.window.title = 'Преобразование'

        self.topframe = Frame(self.window)
        self.midframe = Frame(self.window)
        self.bottomframe = Frame(self.window)

        self.label = Label(self.topframe, text='Введите кол-во км:')
        self.entry = Entry(self.topframe)

        self.label.pack(side='left')
        self.entry.pack(side='left')

        self.show_miles = Label(self.midframe, text='Преобразовано в мили:')
        self.value = StringVar()
        self.miles_label = Label(self.midframe, textvariable=self.value)

        self.show_miles.pack(side='left')
        self.miles_label.pack(side='left')

        self.btnready = Button(self.bottomframe, text='Преобразовать', command=self.convert)
        self.btnexit = Button(self.bottomframe, text='Выйти', command=self.window.destroy)

        self.btnready.pack(side='left')
        self.btnexit.pack(side='left')

        self.topframe.pack()
        self.midframe.pack()
        self.bottomframe.pack()
        mainloop()
    def convert(self):
        kilometers = float(self.entry.get())
        miles = kilometers * 0.6214
        self.value.set(miles)

if __name__ == '__main__':
    my_gui = MyGUI()