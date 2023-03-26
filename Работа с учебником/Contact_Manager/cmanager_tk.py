from contact import Contact
from time import sleep
from tkinter import Label, Button, Tk, Entry, mainloop



def auth_label():
    def datatofile():
        with open('base.txt', 'a', encoding='utf-8') as file:
            inicials = name.get() + ' ' + phone.get() + '\n'
            if inicials == ' ':
                pass
            else:
                file.write(inicials)
                complete = Label(window, text='Регистрация прошла успешно!', fg='green', font='arial 15')
                complete.place(x=100, y=250)
    name = Entry(window, font='arial 12')
    phone = Entry(window, font='arial 12')
    lname = Label(window, text='Введите имя:')
    lphone = Label(window, text='Введите пароль:')
    ready = Button(window, text='Зарегистрироваться', font='arial 13', command=datatofile)
    ready.place(x=165, y=200)
    name.place(x=160, y=140)
    phone.place(x=160, y=170)
    lname.place(x=70, y=140)
    lphone.place(x=55, y=170)




window = Tk()
window.title('М.Контакт')
window.geometry(f'500x500+{window.winfo_screenwidth() // 2 - 250}+{window.winfo_screenheight() // 2 - 250}')
label = Label(window, text='М.Контакт',
              font='arial 25 bold', width=18, height=2)
login = Button(window, text='Вход', width=18, height=2)
registr = Button(window, text='Регистрация', width=18, height=2, command=auth_label)

registr.place(x=366, y=45)
login.place(x=366)
label.place(x=0, y=0)

mainloop()





























#
#
#
#
# def main():
#
#
#
#     def exit_user():
#         window.destroy()
#     def new_user():
#         def full_reg():
#
#
#                 ndestroy = [name, phone, mail, lname, lphone, lmail, ready, login, registr]
#                 for destr in ndestroy:
#                     destr.destroy()
#                 congregistr = Label(window, text='Поздравляю с регистрацией!')
#                 congregistr.place(x=150, y=250)
#                 mycontacts[name] = entry
#                 exit_window = Button(window, text='Выйти', width=18, height=2, command=exit_user)
#                 exit_window.place(x=366)
#
#             else:
#                 print('Это имя уже существует')
#         name = Entry(window, font='arial 12')
#         phone = Entry(window, font='arial 12')
#         mail = Entry(window, font='arial 12')
#         lname = Label(window, text='Имя')
#         lphone = Label(window, text='Номер')
#         lmail = Label(window, text='Эл.Почта')
#         ready = Button(window, text='Зарегистрироваться', font='arial 13', command=full_reg)
#         ready.place(x=105, y=230)
#         name.place(x=100, y=140)
#         phone.place(x=100, y=170)
#         mail.place(x=100, y=200)
#         lname.place(x=70, y=140)
#         lphone.place(x=55, y=170)
#         lmail.place(x=40, y=200)
#     def auth_user():
#         def auth():
#             pass
#
#         lname = Label(window, text='Введите имя:')
#         name = Entry(window, font='arial 12')
#         ready = Button(window, text='Вход')
#         ready.place(y=140, x=260)
#         name.place(x=100, y=140)
#         lname.place(x=25, y=140)
#
#     window = Tk()
#     window.title('Contact Manager')
#     window.geometry(f'500x500+{window.winfo_screenwidth() // 2 - 250}+{window.winfo_screenheight() // 2 - 250}')
#     label = Label(window, text='М.Контакт',
#                   font='arial 25 bold', width=18, height=2)
#     login = Button(window, text='Вход', width=18, height=2, command=auth_user)
#     registr = Button(window, text='Регистрация', width=18, height=2, command=new_user)
#
#     registr.place(x=366, y=45)
#     login.place(x=366)
#     label.place(x=0, y=0)
#
#     mainloop()










