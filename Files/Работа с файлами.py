# phone = open('Call_book.txt', 'r', encoding='utf-8' )
# print(phone.read())
# phone.close()

# with open('Call_book.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)

# with open('Call_book.txt', 'r', encoding='utf-8') as file:
#     count = 0
#     for line in file:
#         count += 1
#         if count % 2 == 0:
#             print(line)

# with open('Call_book.txt', 'a', encoding='utf-8') as file:
#     file.write('Вася Пупкин 8934-541')
#     file.write('\nОлег Близорук')
#     file.write('\nВлад Четвероглазый')
#     file.close()
#
# with open('Call_book.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

#
# import random
# spisok = []
# for i in range(10):
#     spisok.append(random.randint(0, 10))
# with open('Текстовый_Файл.txt', 'w', encoding='utf-8') as file2:
#     for line in spisok:
#         line = str(line)+ '\n'
#         file2.write(line)
#         print(line)

#ДЗ
# with open('Числа.txt', 'w', encoding='utf-8') as file2:
#     for i in range(3):
#         v = input("Введи любое слово:")
#         if len(v) > 3 and len(v) < 8:
#             file2.write(f'\n{v}')
# with open('Числа.txt', 'r', encoding='utf-8') as file:
#      print(file.read())
#
def base():
    while True:
        print('     ------Приветствуем вас в Базе данных завода им.Олег--------')
        print(f'В базе данных, вы можете:'
              f'\n1 - Добавить пользователя'
              f'\n2 - Вывести всю базу данных'
              f'\n3 - Открыть поисковую систему данных конкретного пользователя'
              f'\n0 - Выйти из программы')
        choise = int(input('\nВаш выбор:'))
        if choise == 1:
            add_user()
        elif choise == 2:
            read()
        elif choise == 3:
            search()
        elif choise == 0:
            break
        else:
            print('Такого выбора не существует!')



def add_user():
    with open ('name.txt', 'a', encoding='utf') as file:
        mas = ''
        mas += (input('Введите ваше имя: '))
        mas += ' '
        mas += (input('Введите ваш номер телефона: '))
        mas += ' '
        mas += (input('Введите город проживания: '))
        file.write(mas)


def read():
    with open('name.txt', 'r', encoding='utf') as file:
        for line in file:
            print(line)



#КОНВЕРТАЦИЯ В СПИСОК МЕТОД И РАЗДЕЛЕНИЕ ДАННЫХ ПО ПРОБЕЛУ - split()
with open ('name.txt', 'r', encoding='utf') as file:
    for line in file:
        word = line.split()

        if word[2] == 'мужской':
            print(line)
        if int(word[1]) < 35:
            print(line)
        if 'мужской' in word:
            print(line)



def search():
    with open ('name.txt', 'r', encoding='utf') as file:
        print('----Приветсвуем вас в Поисковой Системе базы данных завода им.Олег----')
        choise = int(input(f'1 - по имени'
                           ' \n2 - по номеру телефона'
                           ' \n3 - по возрасту: '))
        if choise == 1:
            name = input('Введите искомое имя: ')
            for line in file:
                word = line.split(' ')
                if name in word[0]:
                    print(line)
        elif choise == 2:
            phone = input('Введите искомый номер телефона: ')
            for line in file:
                word = line.split()
                if phone in word:
                    print(line)

base()



# with open ('name.txt', 'r', encoding='utf') as file:
#     choise = int(input('1 - Поиск по имени, 2 - Поиск по номеру телефона: '))
#     if choise == 1:
#         name = input('Введите искомое имя: ')
#         for line in file:
#             word = line.split()
#             if name in word:
#                 print(line)
#     elif choise == 2:
#         phone = input('Введите искомый номер телефона: ')
#         for line in file:
#             word = line.split()
#             if phone in word:
#                 print(line)

# def regestr():
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     if ('@yandex.ru' in login or '@gmail.com' in login) and len(password) > 5:
#         with open('login.txt', 'r') as file:
#             for line in file:
#                 q = line.split()
#                 if login == q[0] or password == [1]:
#                     print('Вы ввели занятые данные')
#                     quit()

#         with open('login.txt', 'a', encoding='utf') as file:
#             word = f'{login} {password} \n'
#             file.write(word)
#             print('Данные успешно добавлены')




# regestr()

# from random import randint
# with open('number.txt', 'w')as file:
#     for i in range(100000):
#         file.write(str(randint(1,9999)))
#         file.write('\n')


# with open('Books.txt', 'a')as file:
#     name_books = input('Введите название книги: ')
#     name_author = input('Введите фамилию автора: ')
#     genre_books = input('Введите жанр книги: ')
#     lines = name_books + ' ' + name_author + ' ' + genre_books + '\n'
#     file.writelines(lines)

#
# from random import randint
#
# def ret():
#     with open('Numbers.txt', 'w')as file:
#         file.write('')
#         print('Операция очистки базы данных - прошла успешно!')
#
# def number_add():
#     with open('Numbers.txt', 'a')as file:
#         for i in range(150):
#             file.write(f'{randint(0,200)} \n')
#         print('Данные внесены в систему')
#
# def info():
#     sklad_line = 0
#     number_line = 0
#     with open('Numbers.txt', 'r')as file:
#         for line in file:
#             sklad_line += 1
#             number_line += int(line)
#         print(f'Количество чисел: {sklad_line}\n'
#               f'Сумма чисел: {number_line}')
#
# while True:
#     print(f'1. Очистить файл\n'
#           f'2. Добавить в файл 150 цифр\n'
#           f'3. Вывести данные файла\n'
#           f'4. Выход')
#     ch = int(input('Сделайте выбор: '))
#
#     if ch == 1:
#         ret()
#     elif ch == 2:
#         number_add()
#     elif ch == 3:
#         info()
#     elif ch == 4:
#         print('До Встречи!')
#         break
#     else:
#         print('Такого выбора не существует\n')


# MIN_CHOISE = 1
# MAX_CHOISE = 5
# a = 5
# b = 'Hello'
# w = int(input('Сделайте выбор: '))
# if (w < MIN_CHOISE) and (w > MAX_CHOISE):
#     print('Не корректные данные')
# def catalog():
#     with open('catalog.txt', 'r', encoding='utf-8')as file:
#         for line in file:
#             q = line.split('!')
#             if len(q) > 2:
#                 print(f'Произведение {q[0]}'
#                       f' автор {q[1]}'
#                       f' жанр {q[2]}'
#                       f' год выпуска {q[3]} ')
#
#
#
#
#
# ch = ''
# while ch != '0':
#     ch = input('1 - вывести весь каталог\n2 - добавить книгу\n0 - Выход\n>:')
#     if ch == '1' or ch == '0':
#         catalog()
#
#     elif ch == '2' or ch == '0':
#         pass
#
#     else:
#         print('Не корректные данные')

    # q = int(input('1 - Продолжить, 0 - выйти'))
    # if q == 0:
    #     break

#1.	Функция добавления гостя в базу данных гостей
#Пользователь вводит ФИО, свой пол и телефонный номер. Мы добавляем данные в файл.
#
#
#
#
#
# def guest_freeroom():
#     i = 0
#     with open('clients.txt', 'r', encoding='utf-8')as f:
#         for line in f:
#             i += 1
#         print(f'Всего свободных номеров {200 - i}')
#
# def guest_add():
#     guest_freeroom()
#     with open('clients.txt', 'a', encoding='utf-8')as file:
#         fio = input('Введите свое ФИО: ')
#         gender = input('Введите свой пол(м или ж): ')
#         phone = input('Введите свой телефонный номер: ')
#         info_guest = fio + ' ' + gender + ' ' + ' ' + phone
#         file.write(f'{info_guest} \n')
#         print('Вы успешно зарегистрировались!')
#
# def guest_read():
#     with open('clients.txt', 'r', encoding='utf-8')as file:
#             for line in file:
#                 data = line.split()
#                 print(f'Фио гостя: {data[0]} {data[1]} {data[2]}   '
#                       f'Пол гостя: {data[3]}   '
#                       f'Телефонный номер гостя: {data[4]}')
#
# def guest_services():
#     with open('services.txt', 'r', encoding='utf-8')as file:
#         print('Услуга           Стоимость')
#         for line in file:
#             print(line)
#
# def guest_add_services():
#     with open('services.txt', 'a', encoding='utf-8')as file:
#         name = input('Введите название услуги: ')
#         money = input('Введите стоимость услуги: ')
#         info_serv = name + ' ' + money
#         file.write(f'{info_serv} \n')
#
#
# while True:
#     choise = input('1. Купить номер\n'
#                        '2. Услуги отеля\n'
#                        '3. Забронированные номера\n'
#                        '4. Добавить услугу\n'
#                        '0. Выйти\n'
#                        '>:')
#     if choise == '1':
#         guest_add()
#     elif choise == '2':
#         guest_services()
#     elif choise == '3':
#         guest_read()
#     elif choise == '4':
#         guest_add_services()
#     elif choise == '0':
#         break
#     else:
#         print('Данного выбора не существует!!!')




































