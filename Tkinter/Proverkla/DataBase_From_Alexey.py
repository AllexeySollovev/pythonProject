from tkinter import *
from random import choice
from tkinter.filedialog import *
def open_full_base():
    path = askopenfilename()
    if path != '':
        with open(path, 'r', encoding='utf-8')as file:
            count = 1
            base = ''
            for line in file:
                people = line.split('!')
                base = base + f'{count}.' \
                       f' ФИО:{people[0]}' \
                       f',Номер:{people[1]}' \
                       f',Дата рождения:{people[2]}' \
                       f',Город:{people[3]}' \
                       f',Место работы:{people[4]}'
                count += 1
            peoples = Toplevel()
            info_peoples = Text(peoples, wrap=WORD, width=175, height=50)
            info_peoples.insert(1.0, base)
            info_peoples.config(state=DISABLED)

            info_peoples.pack(fill=BOTH, side=LEFT, expand=True)
            scroll = Scrollbar(peoples ,command=info_peoples.yview)
            scroll.pack(fill=Y, side=RIGHT)
            info_peoples.config(yscrollcommand=scroll.set)

def info_random_people():
    path = askopenfilename()
    if path != '':
        with open(path, 'r', encoding='utf-8')as file:
            data_base = file.readlines()
            people = choice(data_base).split('!')
            window_people = Toplevel()
            label = Label(window_people, text=f'ФИО: {people[0]}\n'
                                              f'Номер: {people[1]}\n'
                                              f'Дата рождения: {people[2]}\n'
                                              f'Город: {people[3]}\n'
                                              f'Место работы: {people[4]}', font='bald')
            label.pack()

window = Tk()

lab_base = Label(window, text='Hacker БД')
random_people = Button(window, text='Вывод случайного человека', width=23, command=info_random_people)
full_base = Button(window, text='Посмотреть базу', width=23, command=open_full_base)
exit_programm = Button(window, text='Выход', command=window.destroy, width=23)

lab_base.pack()
random_people.pack()
full_base.pack()
exit_programm.pack()

mainloop()