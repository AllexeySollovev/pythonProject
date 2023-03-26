# from tkinter import *
#
# window = Tk()
#
# def insert_text():
#     big_text = f'Наступила осень\n' \
#                f'Пожелтел наш сад\n' \
#                f'Листья на березе\n' \
#                f'Золотом горят\n'
#     text.insert(1.0, big_text)
# def get_text():
#     label['text'] = text.get(1.0, END)
# def delete_text():
#     text.delete(1.0, END)
#
#
# text = Text(width=50,
#             height=9,
#             background='darkgreen',
#             foreground='white',
#             wrap=WORD)
#
# b1 = Button(window, text='Вставить текст', width=25, command=insert_text)
# b2 = Button(window, text='Скопировать текст', width=25, command=get_text)
# b3 = Button(window, text='Очистить поле', width=25, command=delete_text)
#
# label = Label(window, width=25, height=5)
# text.pack()
# b1.pack()
# b2.pack()
# b3.pack()
# label.pack()
#
# mainloop()

# from tkinter import *
#
# window = Tk()
# text = Text(width=25, height=5)
# text.pack(side=LEFT)
#
# scroller = Scrollbar(command=text.yview)#Создание скроллбара, задаем прокрутку по оси Y
# scroller.pack(side=LEFT, fill=Y) #Привязка скроллера по левому краю + растягивание его по оси Y
# text.config(yscrollcommand=scroller.set) #Связываем text и скроллер по оси Y
#
# mainloop()

# from tkinter import *
# window = Tk()
# main_menu = Menu(window,)
# window.config(menu=main_menu)
#
# file_menu = Menu(main_menu, tearoff=0)
# file_menu.add_command(label='Открыть')
# file_menu.add_command(label='Сохранить')
# file_menu.add_command(label='Выход')
#
# help_menu = Menu(main_menu, tearoff=0)
# help_menu.add_command(label='Помощь')
# help_menu.add_command(label='О программе')
#
#
# main_menu.add_cascade(label='Файл', menu=file_menu)
# main_menu.add_cascade(label='Справка', menu=help_menu)
#
# text = Text(width=25, height=5)
# text.pack(side=LEFT)
#
#
#
#
#
# mainloop()

from tkinter import *

def save_file():
    name_save = path_enter.get() #получение названия файла из Entry
    Ist = text.get(1.0, END).split('\n')
    with open(name_save + '.txt', 'w', encoding='utf-8')as file:
        for i in Ist:
            file.write(i + '\n')


def open_file():
    name = path_enter.get()
    with open(name, 'r', encoding='utf-8')as file:
        lst = file.readlines()
    text.delete(1.0, END)
    text.insert(1.0, ''.join(lst))


window = Tk()
window.title('Блокнот им.Алексея')
window.geometry('600x700')

main_menu = Menu(window)

window.config(menu=main_menu)

#Создание главного окна и меню
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)

#Добавляет линию разделитель в меню
file_menu.add_separator()
file_menu.add_command(label='Выход', command=window.destroy)

help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label='О программе')

main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Справка', menu=help_menu)

path_enter =  Entry(window)
path_enter.pack(fill=X)
text = Text(window, width=1, height=1, wrap=WORD, font='arial 15')
text.pack(fill=BOTH, side=LEFT, expand=True)

scroll = Scrollbar(command=text.yview)
scroll.pack(fill=Y, side=LEFT)
text.config(yscrollcommand=scroll.set)





mainloop()