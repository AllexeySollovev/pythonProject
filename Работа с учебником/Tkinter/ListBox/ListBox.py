from tkinter import *
class ListboxExample:
    def __init__(self):
        self.window = Tk()

        self.listbox = Listbox(self.window, width=0, height=0)
        self.listbox.pack(pady=10, padx=10)
        self.delete_btn = Button(self.window, text='Удалить выбранный элемент', command=self.click_button)
        self.delete_btn.pack(pady=5, padx=5)
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

        for day in days:
            self.listbox.insert(END, day)
        mainloop()
    def click_button(self):
        self.listbox.delete(ACTIVE)
if __name__ == '__main__':
    listbox = ListboxExample()