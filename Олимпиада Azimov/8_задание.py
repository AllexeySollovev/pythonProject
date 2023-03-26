from time import sleep
def verify_menu():
    print('Добро пожаловать в меню\n'
          'Всё что вы можете сделать\n')
    while True:
        choise = int(input('1 - Добавить пользователя\n'
                           '2 - Найти сотрудника\n'
                           '0 - Выход из системы\n'
                           'Ввод:'))
        if choise == 1:
            with open('database.txt', 'a', encoding='utf-8')as file:
                fio = (input('Введите Фио сотрудника: '))
                phone = (input('Номер телефона сотрудника(89046372903): '))
                family = (input('Семейное положение сотрудника: '))
                post = (input('Должность сотрудника: '))
                date = (input('Дата трудоуйстройства сотрудника(день.месяц.год): '))
                data = fio + ' ' + phone + ' ' + family + ' ' + post + ' ' + date
                file.write(f'\n{data}')
        elif choise == 0:
            break






countmiss = 0
while countmiss != 5:
    login = input('Введите логин:')
    password = input('Введите пароль:')

    with open('data.txt', 'r')as file:
        for line in file:
            data = line.split()

            if countmiss == 3:
                print('Вам запрещено вводить данные на 5 минут,\nтак как вы допустили уже 3 ошибки ')
                sleep(300)
            elif data[0] != login or data[1] != password:
                print('Регистрация данных в базу...')
                sleep(3)
                if set(login) & set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя!-?'):
                    print('Вы допустили ошибку регистра логина!!!')
                    countmiss += 1

                else:
                    if len(password) > 10 or\
                    len(password) < 6 or\
                    set(password) & set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') or\
                    password.islower():
                        print('Вы допустили ошибку регистра пароля!!!')
                        countmiss += 1

                    else:
                        with open('data.txt', 'a', encoding='utf-8')as file:
                            dates = login + ' ' + password + '\n'
                            file.write(f'{dates}')
                        verify_menu()

            else:
                verify_menu()








