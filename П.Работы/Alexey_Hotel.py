guests = 10
def guest_add():
    global guests
    with open('clients.txt', 'a', encoding='utf-8')as file:
        free_room = 200 - guests
        print(f'Всего свободных номеров {free_room} ')
        fio = input('Введите свое ФИО: ')
        gender = input('Введите свой пол(м или ж): ')
        phone = input('Введите свой телефонный номер: ')
        info_guest = fio + ' ' + gender + ' ' + ' ' + phone
        file.write(f'{info_guest} \n')
        print('Вы успешно зарегистрировались!')
        guests += 1

def guest_read():
    with open('clients.txt', 'r', encoding='utf-8')as file:
            for line in file:
                data = line.split()
                print(f'Фио гостя: {data[0]} {data[1]} {data[2]}   '
                      f'Пол гостя: {data[3]}   '
                      f'Телефонный номер гостя: {data[4]}')

def guest_services():
    with open('services.txt', 'r', encoding='utf-8')as file:
        print('Услуга           Стоимость')
        for line in file:
            print(line)

def guest_add_services():
    with open('services.txt', 'a', encoding='utf-8')as file:
        name = input('Введите название услуги: ')
        money = input('Введите стоимость услуги: ')
        info_serv = name + ' ' + money
        file.write(f'{info_serv} \n')


while True:
    choise = input('1. Купить номер\n'
                       '2. Услуги отеля\n'
                       '3. Забронированные номера\n'
                       '4. Добавить услугу\n'
                       '0. Выйти\n'
                       '>:')
    if choise == '1':
        guest_add()
    elif choise == '2':
        guest_services()
    elif choise == '3':
        guest_read()
    elif choise == '4':
        guest_add_services()
    elif choise == '0':
        break
    else:
        print('Данного выбора не существует!!!')