from tkinter import *


class ScrollListBox:
    def __init__(self):
        self.window = Tk()

        self.listbox_frame = Frame(self.window)
        self.listbox_frame.pack(padx=5, pady=5)

        self.listbox = Listbox(self.listbox_frame, height=0, width=20)
        self.listbox.pack(side='top')

        self.scroll = Scrollbar(self.listbox_frame, orient=HORIZONTAL)
        self.scroll.pack(side='bottom', fill=X)

        self.scroll.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scroll.set)

        months = ['Небоскреб Бурдж-Халифа имеет высоту 2717 футов.',
                  'Шанхайская башня имеет высоту 2073 фута.',
                  'Часовая башня Абрадж Аль-бейт имеет высоту 1971 фут.',
                  'Финансовый центр Пинань имеет высоту 1965 футов']
        for month in months:
            self.listbox.insert(END, month)

        mainloop()


if __name__ == '__main__':
    scrollbar = ScrollListBox()
