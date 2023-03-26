#метод get()
# phone = {'model': 'phone', 'color': 'red', 'camera': '12'}
# # point_value = phone.get('screen', 'Такого ключа нет')
# # print(phone.get('screen', 'Такого ключа нет'))
# key = input('Введите параметр для поиска: ')
# q = phone.get(key, 'FALSE')
# if q == 'FALSE':
#     print('К сожалению, ошибка')
# else:
#     print('Данные успешно найдены', phone[key])


#метод items()
# phone = {'model': 'phone', 'color': 'red', 'camera': '12'}
# for key, value in phone.items():
#     print(f'{key} | {value}')


#метод keys()
# phone = {'model': 'phone', 'color': 'red', 'camera': '12'}
# for k in phone.keys():
#     print(k)
#
# people = {'Андрей': 'Охранник',
#           'Нина': 'Кассир',
#           'Олег': 'Консультант',
#           'Олеся': 'Мендежер'}
# while True:
#     name = input('Введите имя сотрудника(Для проверки): ')
#     if name not in people.keys():
#         print(f'Данных о сотруднике {name} в базе нет')
#         positions = input('Введите должность сотрудника: ')
#         people[name] = positions
#         print(people)
#     else:
#         print(f'Сотрудник {name} Зарплата начислена')
#     ch = input('Закончить использование програмы? 1 - Да')
#     if ch == '1':
#         print('Пока')
#         break
#
#Метод sortred()
# people = {'Андрей': 'Охранник',
#           'Нина': 'Кассир',
#           'Олег': 'Консультант',
#           'Олеся': 'Мендежер'}
# for name in sorted(people.keys()):
#     print(name)
# #Метод values()
# for name in sorted(people.values()):
#     print(name)


# people = {'Андрей': 'Охранник',
#           'Нина': 'Кассир',
#           'Олег': 'Консультант',
#           'Олеся': 'Мендежер',
#           'Кирилл': 'Мендежер',
#           'Григорий': 'Директор'}
# #Метод set()
# for name in set(people.values()):
#     print(name)


def shop():
    import time
    shopgame = {'Rust': 3000, 'Dota 2': 400, 'GTA VI': 4000}
    while True:
        print()
        print('=== ИНТЕРНЕТ МАГАЗИН "У ОЛЕГА" ===')
        print('Вы можете сортировать игры по вашему желанию:')
        print('1. Вывод всех данных(игры и стоимость)')
        print('2. Вывод всех игр')
        print('3. Вывод только стоимости')
        print('0. Выход из магазина')
        print()
        choice = int(input('Ваш выбор: '))
        if choice == 1:
            for key,value in shopgame.items():
                print(f'Игра {key}|{value} рублей')
            time.sleep(3)
        elif choice == 2:
            print('Игры нашего магазина:')
            for key in shopgame.keys():
                print(key)
            time.sleep(3)
        elif choice == 3:
            print('Все стоимости нашего магазина: ')
            for val in shopgame.values():
                print(f'{val} рублей')
            time.sleep(3)
        elif choice == 0:
            break
shop()



