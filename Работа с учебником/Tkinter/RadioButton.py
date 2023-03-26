from tkinter import *
from tkinter.messagebox import *

class MyGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title = 'RadioButton'

        self.topframe = Frame(self.window)
        self.bottomframe = Frame(self.window)

        self.radio = IntVar()
        self.radio.set(0)

        self.var1 = Radiobutton(self.topframe, text='Вариант 1', variable=self.radio, value=1)
        self.var2 = Radiobutton(self.topframe, text='Вариант 2', variable=self.radio, value=2)
        self.var3 = Radiobutton(self.topframe, text='Вариант 3', variable=self.radio, value=3)

        self.var1.pack()
        self.var2.pack()
        self.var3.pack()

        self.ok_button = Button(self.bottomframe, text='ОК', command=self.ok_variable)
        self.quit_button = Button(self.bottomframe, text='Выйти', command=self.window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.topframe.pack()
        self.bottomframe.pack()

        mainloop()

    def ok_variable(self):
        showinfo('Выбор', f'Выбран вариант: {str(self.radio.get())}')

if __name__ == '__main__':
    mygui = MyGUI()