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
    print('--------Админ Меню "Факультеты"-------')
    print('1. Создать новый факультет\n'
          '2. Найти факультет\n'
          '3. Обновить существующий факультет\n'
          '4. Удалить факультет\n'
          '5. Вывести все факультеты\n'
          '6. Выйти\n')


def get_choice():
    choice = int(input('Ваш выбор:> '))
    while choice < MIN or choice > MAX:
        choice = int(input('Ваш выбор:> '))
    return choice

def create():
    name = input('Введите название факультета: ')
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()

        cur.execute('''insert into Departments (Name)
        values (?)''', (name,))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            print('Факультет добавлен.')
            sleep(2)

def read():
    name = input('Введите название искомого факультета: ')
    count = display_major(name)
    print(f'{count} строк найдено.')
    sleep(2)

def update():
    read()

    id_select = int(input('Введите ID факультета: '))
    new_name = input('Введите новое название факультета: ')
    count = update_row(id_select, new_name)
    print(f'{count} строк обновлено.')
    sleep(2)

def delete():
    read()

    id_select = int(input('Ведите ID удаляемого факультета:'))
    count = delete_row(id_select)
    print(f'{count} строк удалено.')
    sleep(2)

def list_majors():
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()
        cur.execute('''select * from Departments''')
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

        cur.execute('''select * from Departments
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
        cur.execute('''update Departments
        set Name = ?
        where DepID == ?''', (name, id))
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
        cur.execute('''delete from Departments
        where DepID == ?''', (id,))
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

