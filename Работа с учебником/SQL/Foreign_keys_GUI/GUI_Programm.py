import sqlite3
from tkinter import *
from tkinter.messagebox import *

class EmployeesInfo:
    def __init__(self):
        self.window = Tk()

        self.__build_window()

        mainloop()

    def __build_window(self):
        self.__build_label()

        self.__build_listbox_frame()

        self.__build_quit_button()

    def __build_label(self):
        self.plabel = Label(self.window, text='Информация о сотрудниках')
        self.plabel.pack(side='top', pady=5, padx=5)

    def __build_listbox_frame(self):
        self.listbox_frame = Frame(self.window)

        self.__setup_listbox()

        self.__setup_scroll()

        self.__pop_listbox()

        self.listbox_frame.pack()

    def __setup_listbox(self):
        self.listbox = Listbox(self.listbox_frame,
                               selectmode=SINGLE,
                               height=6)
        self.listbox.bind("<<ListboxSelect>>", self.__get_details)
        self.listbox.pack(side='left', padx=5, pady=5)

    def __setup_scroll(self):
        self.scrollbar = Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side='right', fill=Y)

    def __pop_listbox(self):
        for employee in self.__get_employee():
            self.listbox.insert(END, employee)

    def __build_quit_button(self):
        self.qbutton = Button(self.window, text='Выйти', command=self.window.destroy)
        self.qbutton.pack(side='top', padx=10, pady=5)

    def __get_employee(self):
        employeel = []
        conn = None
        try:
            conn = sqlite3.connect('employees.db')
            cur = conn.cursor()
            cur.execute('select Name from Employees')

            employeel = [n[0] for n in cur.fetchall()]
        except sqlite3.Error as err:
            showerror('Error', f'Ошибка БД\n{err}')
        finally:
            if conn != None:
                conn.close()
            return employeel

    def __get_details(self, event):
        listbox_index = self.listbox.curselection()[0]
        select_emp = self.listbox.get(listbox_index)

        conn = None

        try:
            conn = sqlite3.connect('employees.db')
            cur = conn.cursor()

            cur.execute(
                '''select
                    Employees.Name,
                    Employees.Position,
                    Departments.DepartmentName,
                    Locations.City
                from
                    Employees, Departments, Locations
                where
                    Employees.Name = ? and
                    Employees.DepartmentID = Departments.DepartmentID and
                    Employees.LocationID = Locations.LocationID''',
                (select_emp,))
            results = cur.fetchone()
            self.__display_details(name=results[0],
                                   position=results[1],
                                   department=results[2],
                                   location=results[3])
        except sqlite3.Error as err:
            showerror('Error', f'Ошибка БД\n{err}')

        finally:
            if conn != None:
                conn.close()

    def __display_details(self, name, position, department, location):
        showinfo('Информация о сотруднике',
                 f'Имя: {name}\n'
                 f'Должность: {position}\n'
                 f'Отдел: {department}\n'
                 f'Местоположение: {location}')

if __name__ == '__main__':
    employee = EmployeesInfo()