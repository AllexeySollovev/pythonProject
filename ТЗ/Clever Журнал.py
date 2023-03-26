from tkinter import *
import time


def btnclick():
    phone = entry_phone.get()
    phone1 = phone.isdigit()
    if first_name.get() == '' or last_name.get() == '':
        label_name['text'] = 'Введите имя прежде чем нажимать на кнопку!!!'
    elif not phone1:
        label_phone['text'] = 'номер телефона введён неккоректно'
    elif '@' not in entry_email.get():
        label_email['text'] = 'вы ввели неккоректный адрес почты'
    elif len(entry_password.get()) < 8:
        label_password['text'] = 'пароль введён неккоректно'
    else:
        label_confirm['text'] = 'Ваши данные были занесены в файл'
        btn['bg'] = 'green'
        data = f'Name - {first_name.get()}; LastName - {last_name.get()};' \
               f' phone - {phone};' \
               f' email - {entry_email.get()};' \
               f' password - {entry_password.get()}\n'
        with open('database.txt', 'a', encoding='utf-8')as f:
            f.write(data)
        time.sleep(2)
        label_name['text'] = 'Введите ваше ФИ ниже'
        label_phone['text'] = 'Введите ваш номер телефона ниже (пример:89046372903)'
        label_email['text'] = 'Введите вашу электронную почту ниже'
        label_password['text'] = 'Введите ваш пароль ниже'
        first_name.delete(0, END)
        last_name.delete(0, END)
        entry_phone.delete(0, END)
        entry_email.delete(0, END)
        entry_password.delete(0, END)




window = Tk()
window.geometry('500x650')
window.title('Умный журнал')
window.configure(bg='gray')
window.resizable(False, False)
first_name = Entry(window, font='arial 15', justify=CENTER)
last_name = Entry(window, font='arial 15', justify=CENTER)
entry_phone = Entry(window, font='arial 15', justify=CENTER)
entry_email = Entry(window, font='arial 15', justify=CENTER)
entry_password = Entry(window, font='arial 15', justify=CENTER, show='*')

label_name = Label(window, text='Введите ваше ФИ ниже', font='arial 12', bg='gray')
label_phone = Label(window, text='Введите ваш номер телефона ниже (пример:89046372903)', font='arial 12', bg='gray')
label_email = Label(window, text='Введите вашу электронную почту ниже', font='arial 12', bg='gray')
label_password = Label(window, text='Введите ваш пароль ниже', font='arial 12', bg='gray')
label_confirm = Label(window, text='', font='arial 12', bg='gray')

first_name.place(anchor=CENTER, x=250, y=65, width=500, height=55)
last_name.place(anchor=CENTER, x=250, y=120, width=500, height=55)
entry_phone.place(anchor=CENTER, x=250, y=225, width=500, height=55)
entry_email.place(anchor=CENTER, x=250, y=330, width=500, height=55)
entry_password.place(anchor=CENTER, x=250, y=435, width=500, height=55)

label_name.place(anchor=CENTER, x=250, y=20)
label_phone.place(anchor=CENTER, x=250, y=175)
label_email.place(anchor=CENTER, x=250, y=280)
label_password.place(anchor=CENTER, x=250, y=385)
label_confirm.place(anchor=CENTER, x=250, y=600)

btn = Button(window, text='Проверить Данные', font='arial 18', command=btnclick)
btn.place(anchor=CENTER, x=250, y=520, width=500, height=90)

window.mainloop()
