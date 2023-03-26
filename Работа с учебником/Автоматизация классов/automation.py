from tkinter import filedialog
from tkinter import *

def ready():
    count = int(input('Сколько атрибутов должно быть в классе: '))
    if count == 4:
        Class = input('Введите название класса: ')
        num1 = input('Введите атрибут №1: ')
        num2 = input('Введите атрибут №2: ')
        num3 = input('Введите атрибут №3: ')
        num4 = input('Введите атрибут №4: ')
        atributes = f'class {Class}:\n' \
                    f'    def __init__(self, {num1}, {num2}, {num3}, {num4}):\n' \
                    f'        self.__{num1} = {num1}\n' \
                    f'        self.__{num2} = {num2}\n' \
                    f'        self.__{num3} = {num3}\n' \
                    f'        self.__{num4} = {num4}\n' \
                    f'\n' \
                    f'    def set_{num1}(self, {num1}):\n' \
                    f'        self.__{num1} = {num1}\n' \
                    f'\n' \
                    f'    def set_{num2}(self, {num2}):\n' \
                    f'        self.__{num2} = {num2}\n' \
                    f'\n' \
                    f'    def set_{num3}(self, {num3}):\n' \
                    f'        self.__{num3} = {num3}\n' \
                    f'\n' \
                    f'    def set_{num4}(self, {num4}):\n' \
                    f'        self.__{num4} = {num4}\n' \
                    f'\n' \
                    f'    def get_{num1}(self):\n' \
                    f'        return self.__{num1}\n' \
                    f'\n' \
                    f'    def get_{num2}(self):\n' \
                    f'        return self.__{num2}\n' \
                    f'\n' \
                    f'    def get_{num3}(self):\n' \
                    f'        return self.__{num3}\n' \
                    f'\n' \
                    f'    def get_{num4}(self):\n' \
                    f'        return self.__{num4}\n'

    elif count == 3:
        Class = input('Введите название класса: ')
        num1 = input('Введите атрибут №1: ')
        num2 = input('Введите атрибут №2: ')
        num3 = input('Введите атрибут №3: ')
        atributes = f'class {Class}:\n' \
                    f'    def __init__(self, {num1}, {num2}, {num3}):\n' \
                    f'        self.__{num1} = {num1}\n' \
                    f'        self.__{num2} = {num2}\n' \
                    f'        self.__{num3} = {num3}\n' \
                    f'\n' \
                    f'    def set_{num1}(self, {num1}):\n' \
                    f'        self.__{num1} = {num1}\n' \
                    f'\n' \
                    f'    def set_{num2}(self, {num2}):\n' \
                    f'        self.__{num2} = {num2}\n' \
                    f'\n' \
                    f'    def set_{num3}(self, {num3}):\n' \
                    f'        self.__{num3} = {num3}\n' \
                    f'\n' \
                    f'    def get_{num1}(self):\n' \
                    f'        return self.__{num1}\n' \
                    f'\n' \
                    f'    def get_{num2}(self):\n' \
                    f'        return self.__{num2}\n' \
                    f'\n' \
                    f'    def get_{num3}(self):\n' \
                    f'        return self.__{num3}\n'
    elif count == 2:
        Class = input('Введите название класса: ')
        num1 = input('Введите атрибут №1: ')
        num2 = input('Введите атрибут №2: ')
        atributes = f'class {Class}:\n' \
                    f'    def __init__(self, {num1}, {num2}):\n' \
                    f'        self.__{num1} = {num1}\n' \
                    f'        self.__{num2} = {num2}\n' \
                    f'\n' \
                    f'    def set_{num1}(self, {num1}):\n' \
                    f'        self.__{num1} = {num1}\n' \
                    f'\n' \
                    f'    def set_{num2}(self, {num2}):\n' \
                    f'        self.__{num2} = {num2}\n' \
                    f'\n' \
                    f'    def get_{num1}(self):\n' \
                    f'        return self.__{num1}\n' \
                    f'\n' \
                    f'    def get_{num2}(self):\n' \
                    f'        return self.__{num2}\n'
    elif count == 1:
        Class = input('Введите название класса: ')
        num1 = input('Введите атрибут №1: ')
        atributes = f'class {Class}:\n' \
                    f'    def __init__(self, {num1}):\n' \
                    f'        self.__{num1} = {num1}\n' \
                    f'\n' \
                    f'    def set_{num1}(self, {num1}):\n' \
                    f'        self.__{num1} = {num1}\n' \
                    f'\n' \
                    f'    def get_{num1}(self):\n' \
                    f'        return self.__{num1}\n'

    print(atributes)
    path = filedialog.asksaveasfilename(defaultextension='txt',
                                        filetypes=(('Текст', '*.txt'), ('Python', '*.py')))  # создаем путь для файла
    if path != '':
        with open(path, 'w', encoding='utf-8') as file:
            for line in atributes:
                file.write(line)
window = Tk()
btn = Button(window, text='Готово', command=ready)
btn.pack()

mainloop()