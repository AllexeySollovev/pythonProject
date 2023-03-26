from tkinter import *
class ListBoxExample:
    def __init__(self):
        self.window = Tk()

        self.listbox = Listbox(self.window, width=0, height=0)
        self.listbox.pack(pady=10, padx=10)
        self.listbox.bind('<<ListboxSelect>>', self.click_button)
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

        for day in days:
            self.listbox.insert(END, day)
        mainloop()

    def click_button(self, event):
        index = self.listbox.curselection()
        self.listbox.delete(index[0])
if __name__ == '__main__':
    listbox = ListBoxExample()