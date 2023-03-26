

# d = {}
# print(d)

# d = {1: 'Павел',2: 'Кирилл',3: 'Кот'}
# print(d[2])

# d = {1: 'Павел','2': True,3: 10.7}
# print(d['2'])

# phonebook = {'мама': 8936,'папа': 8927,'брат': 8920}
# # print(phonebook['мама'])
# choice = input('Хотите обновить список контактов')
# if choice.lower() == 'да':
#     phonebook['сестра'] = 8912
#     print(f'Ваш список успешно обновлён {phonebook}')
# else:
#     w = input(f'Кому вы желаете позвонить {phonebook}?')
#     if w == 'папа':
#         print(f'{phonebook["папа"]}')
#     elif w == 'мама':
#         print(f'{phonebook["мама"]}')
#     elif w == 'брат':
#         print(f'{phonebook["брат"]}')
#     elif w == 'сестра':
#         print(f'{phonebook["сестра"]}')
#
#     else:
#         print('Такого номера нет')


# d = dict()
# d['РОССИЯ'] = 'Москва'
# d['ЯПОНИЯ'] = 'Токио'
# d['КИТАЙ'] = 'Пекин'
#
#
# otvet = input('Введите название страны: ')
# if otvet.upper() in d:
#     print(f'Столица {otvet}: {d[otvet.upper()]}')
# else:
#     print('В словаре нету такой страны')

#
# alien = { }
# print(alien)
# print(type(alien))

# alien = {'color': 'green', 'points': 5}
# print(alien['color'])
# print(alien['points'])
# #alien['class'] = 'human'
# # alien['class'] = input('Введите класс обьекта: ')
# alien['class'] = 'human'
# print(alien)
#
# #Удаление значения из словаря - del
# del alien['points']
# print(alien)

phone = {}
def Dream_Phone():
    print('Добро пожаловать в систему создания вашего телефона')
    phone['model'] = input('Введите название марки вашего телефона: ')
    phone['screen'] = input('Введите тип вашего экрана - OLED LCD: ')
    if phone['screen'] != 'OLED' or phone['screen'] != 'LCD':
        print('Вы ввели неверное значение')
        phone['screen'] = 'OLED'
    phone['color'] = input('Введите цвет телефона')
    phone['camera'] = int(input('Введите Количество мп от 10 до 40: '))
    if 10 > phone['camera'] or phone['camera'] > 40:
        print('Вы ввели неверное значени. Выбрано значение по умолчанию(20мп)')
        phone['camera'] = 20
    print('Ваша модель телефона была успешно собрана!')
    print(phone)

def Remove_Phones():
    key = input('Введите характеристику для удаления')
    if key in phone:
        del phone[key]
        print('Удаление прошло успешно')
        print(phone)
    else:
        print('Такой характеристики нет')

Dream_Phone()
Remove_Phones()













