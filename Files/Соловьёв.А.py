
# 1 задание
# n = input('Введите любые слова: ')
# print(max(n.split(), key=len))
# print(len(n))
#2 задание
#
#
#
# def base():
#     while True:
#         print('     ------Приветствуем вас в Базе данных завода БуКвОеД--------')
#         print(f'В базе данных, вы можете:'
#               f'\n1 - Добавить книгу'
#               f'\n2 - Вывести всю базу данных'
#               f'\n3 - Открыть поисковую систему данных конкретной книги'
#               f'\n0 - Выйти из программы')
#         choise = int(input('\nВаш выбор:'))
#         if choise == 1:
#             add_user()
#         elif choise == 2:
#             read()
#         elif choise == 3:
#             search()
#         elif choise == 0:
#             break
#         else:
#             print('Такого выбора не существует!')
#
#
#
# def add_user():
#     with open ('Books.txt', 'a', encoding='utf') as file:
#         mas = []
#         mas.append(input('Введите название книги: '))
#
#         mas.append(input('Введите жанр книги: '))
#
#         mas.append(input('Введите фамилию автора книги: '))
#         file.write(f'{mas}')
#
#
# def read():
#     with open('Books.txt', 'r', encoding='utf') as file:
#         for line in file:
#             print(line)
#
#
# def search():
#     with open ('Books.txt', 'r', encoding='utf') as file:
#         print('----Приветсвуем вас в Поисковой Системе базы данных завода им.Олег----')
#         choise = int(input(f'1 - по названию'
#                            ' \n2 - по автору'
#                            ' \n3 - по жанру: '))
#         if choise == 1:
#             name = input('Введите название искомой книги: ')
#             for line in file:
#                 if name in line:
#                     print(line)
#                 else:
#                     print('Такого имени в базе данных нету')
#         elif choise == 2:
#             by = input('Введите иского автора книги: ')
#             for line in file:
#                 if by in line:
#                     print(line)
#                 else:
#                     print('Такого имени в базе данных нету')
#         elif choise == 3:
#             name = input('Введите жанр искомой книги: ')
#             for line in file:
#                 if name in line:
#                     print(line)
#                 else:
#                     print('Такого имени в базе данных нету')
# base()

#3 задание
# from random import randint
# summ = 0
# with open('number.txt', 'a')as file:
#     for i in range(150):
#         file.write(str(randint(0,300)))
#         file.write('\n')
#     for line in file:
#         word = line.split()
#         summ += 1

#Очистка файла
# with open('number.txt', 'w')as f:
#     f.write('')
#Разность двух чисел



