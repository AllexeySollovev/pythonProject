# from time import sleep
#
# def read_base():
#     with open('Clients.txt', 'r', encoding='utf-8')as file:
#         for line in file:
#             print(line)
#
# def registration_user():
#     with open('Clients.txt', 'a+', encoding='utf-8')as file:
#         print(f'Добро Пожаловать в компанию Microsoft!\nДопускается до 8 символов в логине и пароле\n'
#               f'Зарегистрируйтесь:')
#         login = input('Введите логин\n>: ')
#         password = input('Введите пароль\n>: ')
#         for line in file:
#             auth = line.split()
#         if len(login) or len(password) <= 8:
#             if login in auth:
#                 print('Вы ввели занятые данные!!!')
#             else:
#                 user = login + ' ' + password
#                 file.write(f'{user}\n')
#                 print('Регистрация прошла успешно!')
#
#         else:
#             print('Ваш логин либо пароль не удовлетворяет правила регистра!\n'
#                   'Повторите попытку')
#
# def search_user():
#     with open('Clients.txt', 'r', encoding='utf-8')as file:
#         print('<Поисковая система Microsoft>')
#         login = input('Введите логин искомого пользователя: ')
#         for line in file:
#             search = line.split()
#             if login in search:
#                 print(line)
#             else:
#                 print('Такого имени нету в базе данных!')
#
# def authorization():
#     with open('Clients.txt', 'r', encoding='utf-8')as file:
#         print('Авторизируйтесь!')
#         key = input('Введите логин: ')
#         password = input('Введите пароль: ')
#         for line in file:
#             registr = line.split()
#             if key in registr[0] or password in registr[1]:
#                 sleep(3)
#                 print('Авторизация прошла успешно!')
#                 sleep(1)
#                 menu()
#
#             else:
#                 print('Логин либо пароль неверны!!!')
#
# def menu():
#     while True:
#         print('Приветствуем вас в панели Разработчика!\n'
#               'Вы можете:')
#         choise = int(input('1. Поиск пользователя\n'
#                            '2. Вывести всю базу данных\n'
#                            '3. Выйти\n'
#                            '>: '))
#         if choise == 1:
#             search_user()
#         elif choise == 2:
#             read_base()
#         elif choise == 3:
#             print('Пока!')
#             break
#         else:
#             print('Такого выбора не существует!!!')
#
#
#
#
#
#
#
#
#
#
# def base():
#     while True:
#         print('Приветствуем вас в компании Microsoft\n')
#         choise = int(input('1. Авторизоваться\n'
#                            '2. Зарегистрироваться\n'
#                            '3. Выйти\n'
#                            '>: '))
#         if choise == 1:
#             authorization()
#         elif choise == 2:
#             registration_user()
#         elif choise == 3:
#             print('Пока!')
#             break
#         else:
#             print('Такого выбора нет!')
# base()

# mil = 0.6214
# km = int(input('Здравствуйте! Сколько вы прошли километров?\n>:'))
# def convert(kilometers,miles):
#     return kilometers * miles
# print(f'Вы прошли {convert(km, mil):.1f} Миль')












