from tkinter import *

MORNING = 10
EVENING = 12
NIGHT = 5


class InterCity:

    def __init__(self):
        self.window = Tk()
        self.window.title('Междугордные звонки')

        self.radio = IntVar()
        self.radio.set(0)

        self.radio1 = Radiobutton(self.window, text='Дневное время (с 6:00 по 17:59)', variable=self.radio, value=1)
        self.radio2 = Radiobutton(self.window, text='Вечернее время (с 18:00 по 23:59)', variable=self.radio, value=2)
        self.radio3 = Radiobutton(self.window, text='Непиковый период (с 24:00 по 5:59)', variable=self.radio, value=3)

        self.radio1.pack(side='top', padx=10)
        self.radio2.pack(side='top', padx=10)
        self.radio3.pack(side='top', padx=10)

        self.top_frame = Frame(self.window)
        self.top_frame.pack(padx=0)

        self.minutes = Label(self.top_frame, text='Кол-во минут:')
        self.entry = Entry(self.top_frame)
        self.btncall = Button(self.top_frame, text='Позвонить', command=self.call)

        self.minutes.pack(side='left')
        self.btncall.pack(side='right')
        self.entry.pack(side='right')

        self.bottom_frame = Frame(self.window)
        self.bottom_frame.pack()

        self.lvar = StringVar()
        self.lvar.set('0р')

        self.label = Label(self.bottom_frame, text='Стоимость звонка:')
        self.labelvar = Label(self.bottom_frame, textvariable=self.lvar)

        self.label.pack(side='left')
        self.labelvar.pack(side='left')

        self.btnexit = Button(self.window, text='Выйти', command=self.window.destroy)
        self.btnexit.pack()

        mainloop()

    def call(self):
        choice = self.radio.get()
        minutes = int(self.entry.get())
        if choice == 1:
            self.lvar.set(f'{minutes * MORNING}')
        elif choice == 2:
            self.lvar.set(f'{minutes * EVENING}')
        elif choice == 3:
            self.lvar.set(f'{minutes * NIGHT}')


if __name__ == '__main__':
    calls = InterCity()
