from tkinter import *


class ScrollListBox:
    def __init__(self):
        self.window = Tk()

        self.listbox_frame = Frame(self.window)
        self.listbox_frame.pack()

        self.listbox = Listbox(self.listbox_frame, height=6, width=0)
        self.listbox.pack(side='left')

        self.scroll = Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scroll.pack(side='right', fill=Y)

        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                  'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        for month in months:
            self.listbox.insert(END, month)

        mainloop()


if __name__ == '__main__':
    scrollbar = ScrollListBox()
