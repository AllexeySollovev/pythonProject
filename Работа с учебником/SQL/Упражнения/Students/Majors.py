import sqlite3
from time import sleep
MIN = 1
MAX = 6
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
MAJORS = 5
EXIT = 6
DATA = 'students.db'

def main():
    choice = 0
    while choice != EXIT:
        get_menu_choice()
        choice = get_choice()
        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice  == DELETE:
            delete()
        elif choice == MAJORS:
            list_majors()

def get_menu_choice():
    print('--------Админ Меню "Специальности"-------')
    print('1. Создать новую специальность\n'
          '2. Найти специальность\n'
          '3. Обновить существующую специальность\n'
          '4. Удалить специальность\n'
          '5. Вывести все специальности\n'
          '6. Выйти\n')


def get_choice():
    choice = int(input('Ваш выбор:> '))
    while choice < MIN or choice > MAX:
        choice = int(input('Ваш выбор:> '))
    return choice

def create():
    name = input('Введите название специальности: ')
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()

        cur.execute('''insert into Majors (Name)
        values (?)''', (name,))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            print('Специальность добавлена.')
            sleep(2)

def read():
    name = input('Введите название искомой специальности: ')
    count = display_major(name)
    print(f'{count} строк найдено.')
    sleep(2)

def update():
    read()

    id_select = int(input('Введите ID специальности: '))
    new_name = input('Введите новое название специальности: ')
    count = update_row(id_select, new_name)
    print(f'{count} строк обновлено.')
    sleep(2)

def delete():
    read()

    id_select = int(input('Ведите ID удаляемой специальности:'))
    count = delete_row(id_select)
    print(f'{count} строк удалено.')
    sleep(2)

def list_majors():
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()
        cur.execute('''select * from Majors''')
        results = cur.fetchall()
        for row in results:
            print(f'ID:{row[0]} - {row[1]} ')
        print(len(results), 'строк найдено.')
    except sqlite3.Error as err:
        print('Ошибка БД ', err)
    finally:
        if conn != None:
            conn.close()
            sleep(2)

def display_major(name):
    name = f'%{name}%'
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()

        cur.execute('''select * from Majors
         where Name like ?''', (name,))
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]} - {row[1]}')
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            return len(results)

def update_row(id, name):
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()
        cur.execute('''update Majors
        set Name = ?
        where MajorID == ?''', (name, id))
        conn.commit()
        count = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            return count

def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()
        cur.execute('''delete from Majors
        where MajorID == ?''', (id,))
        conn.commit()
        count = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            return count

if __name__ == '__main__':
    main()

