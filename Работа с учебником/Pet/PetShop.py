from pet import Pet
from pickle import dump, load
from time import sleep
def main():
    choice = ''
    pets = load_pets()
    while choice != 0:
        choice = int(input('Сделайте выбор:\n'
                           '1 - Посмотреть всех питомцев\n'
                           '2 - Записать своего питомца\n'
                           '0 - Выйти\n'
                           '>:'))
        if choice == 1: list_pets(pets)
        elif choice == 2: add(pets)
def add(pets):
    name = input('Введите имя вашего питомца: ')
    animal_type = input('Введите его тип(кот, собака): ')
    age = int(input('Введите его возраст: '))

    mypet = Pet(name, animal_type, age)

    pets[name] = mypet
    with open('Pets.dat', 'wb')as file:
        dump(pets, file)
def load_pets():
    try:
        with open('Pets.dat', 'rb')as file:
            pets = load(file)
    except IOError and EOFError:
            pets = {}
    return pets
def list_pets(pets):
    for key in pets:
        print(pets[key])
    print('\n')
    sleep(5)
if __name__ == '__main__':
    main()