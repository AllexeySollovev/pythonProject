from tkinter import *


class HorizontVertic:
    def __init__(self):
        self.window = Tk()

        self.outer_frame = Frame(self.window)
        self.outer_frame.pack(padx=5, pady=5)

        self.inner_frame = Frame(self.outer_frame)
        self.inner_frame.pack()

        self.listbox = Listbox(self.inner_frame, height=5, width=30)
        self.listbox.pack(side='left')

        self.v_scroll = Scrollbar(self.inner_frame, orient=VERTICAL)
        self.v_scroll.pack(side='right', fill=Y)

        self.h_scroll = Scrollbar(self.outer_frame, orient=HORIZONTAL)
        self.h_scroll.pack(side='bottom', fill=X)

        self.v_scroll.config(command=self.listbox.yview)
        self.h_scroll.config(command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        data = ['Небоскреб Бурдж-Халифа имеет высоту 2717 футов.',
                'Шанхайская башня имеет высоту 2073 фута.',
                'Часовая башня Абрадж Аль-бейт имеет высоту 1971 фут.',
                'Финансовый центр Пинань имеет высоту 1965 футов',
                'Здание Goldin Finance имеет высоту 1957 футов.',
                'Башня Lotte World имеет высоту 1819 футов.',
                'Всемирный торговый центр 1 имеет высоту 1776 футов.']

        for element in data:
            self.listbox.insert(END, element)

        mainloop()


if __name__ == '__main__':
    hvlistbox = HorizontVertic()