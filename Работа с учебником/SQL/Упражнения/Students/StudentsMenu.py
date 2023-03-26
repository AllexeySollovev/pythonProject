import Majors
import Depart
import Stud
from time import sleep

MIN = 1
MAX = 4
STUDENTS = 1
DEPARTMENTS = 2
MAJORS = 3
EXIT = 4
def main():
    choice = 0
    while choice != EXIT:
        get_menu_choice()
        choice = get_choice()
        if choice == STUDENTS:
            sleep(2)
            Stud.main()
        elif choice == DEPARTMENTS:
            sleep(2)
            Depart.main()
        elif choice == MAJORS:
            sleep(2)
            Majors.main()

def get_menu_choice():
    print('--------Админ Меню-------')
    print('1. Студенты\n'
          '2. Факультеты\n'
          '3. Специальности\n'
          '4. Выход\n ')

def get_choice():
    choice = int(input('Ваш выбор:> '))
    while choice < MIN or choice > MAX:
        choice = int(input('Ваш выбор:> '))
    return choice

if __name__ == '__main__':
    main()
