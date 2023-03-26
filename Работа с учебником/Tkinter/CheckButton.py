from tkinter import *
from tkinter.messagebox import *

class MyGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title = 'RadioButton'

        self.topframe = Frame(self.window)
        self.bottomframe = Frame(self.window)

        self.radio1 = IntVar()
        self.radio2 = IntVar()
        self.radio3 = IntVar()

        self.radio1.set(0)
        self.radio2.set(0)
        self.radio3.set(0)

        self.var1 = Checkbutton(self.topframe, text='Вариант 1', variable=self.radio1)
        self.var2 = Checkbutton(self.topframe, text='Вариант 2', variable=self.radio2)
        self.var3 = Checkbutton(self.topframe, text='Вариант 3', variable=self.radio3)

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
        self.message = 'Вы выбрали:\n'
        if self.radio1.get() == 1:
            self.message = self.message + '1\n'
        if self.radio2.get() == 1:
            self.message = self.message + '2\n'
        if self.radio3.get() == 1:
            self.message = self.message + '3\n'
        showinfo('Выбор', self.message)

if __name__ == '__main__':
    mygui = MyGUI()