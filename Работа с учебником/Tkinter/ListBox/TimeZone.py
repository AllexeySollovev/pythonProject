from tkinter import *


class TimeZone:
    def __init__(self):
        self.window = Tk()
        self.window.title = 'Часовые пояса'

        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()

        mainloop()

    def __build_prompt_label(self):
        self.prompt_label = Label(self.window, text='Выберите город')
        self.prompt_label.pack(padx=5, pady=5)

    def __build_listbox(self):
        self.__cities = ['Денвер', 'Гонолулу', 'Миннеаполис', 'Нью-Йорк', 'Сан-Франциско']
        self.city_listbox = Listbox(self.window, height=0, width=0)
        self.city_listbox.pack(padx=5, pady=5)

        self.city_listbox.bind('<<ListboxSelect>>', self.__display_time_zone)

        for city in self.__cities:
            self.city_listbox.insert(END, city)

    def __build_output_frame(self):
        self.output_frame = Frame(self.window)
        self.output_frame.pack(padx=5)

        self.output_discription_label = Label(self.output_frame, text='Часовой пояс:')
        self.output_discription_label.pack(side='left', padx=(5, 1), pady=5)

        self.__timezone = StringVar()
        self.output_label = Label(self.output_frame, borderwidth=1,
                                  relief='solid', width=20, textvariable=self.__timezone)
        self.output_label.pack(side='right', padx=(1, 5), pady=5)

    def __build_quit_button(self):
        self.quit_button = Button(self.window, text='Выйти', command=self.window.destroy)
        self.quit_button.pack(padx=5, pady=5)

    def __display_time_zone(self, event):
        index = self.city_listbox.curselection()

        city = self.city_listbox.get(index[0])

        if city == 'Денвер':
            self.__timezone.set('Горный')
        elif city == 'Гонолулу':
            self.__timezone.set('Гавайско-алеутский')
        elif city == 'Миннеаполис':
            self.__timezone.set('Центральный')
        elif city == 'Нью-Йорк':
            self.__timezone.set('Восточный')
        elif city == 'Сан-Франциско':
            self.__timezone.set('Тихоокеанский')

if __name__ == '__main__':
    time_zone = TimeZone()