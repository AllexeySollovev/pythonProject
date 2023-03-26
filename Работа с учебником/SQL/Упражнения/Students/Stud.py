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
            info_students()


def get_menu_choice():
    print('--------Админ Меню "Студенты"-------')
    print('1. Добавить студента\n'
          '2. Найти студента\n'
          '3. Обновить данные о студенте\n'
          '4. Удалить данные о студенте\n'
          '5. Показать всех студентов\n'
          '6. Выйти\n')


def get_choice():
    choice = int(input('Ваш выбор:> '))
    while choice < MIN or choice > MAX:
        choice = int(input('Ваш выбор:> '))
    return choice


def create():
    majors_depart()
    name = input('Введите имя студента: ')
    maj = int(input('Введите ID специальности: '))
    dep = int(input('Введите ID факультета: '))
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()

        cur.execute('''insert into Students (Name, MajorID, DepID)
        values (?, ?, ?)''', (name, maj, dep))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            print('Специальность добавлена.')
            sleep(2)


def read():
    name = input('Введите имя студента: ')
    count = display_major(name)
    print(f'{count} строк найдено.')
    sleep(2)


def update():
    read()

    id_select = int(input('Введите ID Студента: '))
    majors_depart()
    new_major = input('Введите новую специальность: ')
    new_dep = input('Введите новый факультет: ')
    count = update_row(id_select, new_major, new_dep)
    print(f'{count} строк обновлено.')
    sleep(2)


def delete():
    read()

    id_select = int(input('Ведите ID удаляемого студента:'))
    count = delete_row(id_select)
    print(f'{count} строк удалено.')
    sleep(2)


def info_students():
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()
        cur.execute(
            '''select
                Students.StuID,
                Students.Name,
                Majors.Name,
                Departments.Name
            from
                Students, Majors, Departments
            where
                Students.MajorID == Majors.MajorID and
                Students.DepID == Departments.DepID''')
        results = cur.fetchall()
        print('   ID     Имя         Специальность            Факультет')
        for row in results:
            print(f'{row[0]:4}   {row[1]:10} {row[2]:25} {row[3]}')
        print(f'{len(results)} строк найдено.')
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()


def majors_depart():
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()
        cur.execute('''select * from Majors''')
        results = cur.fetchall()
        print('Специальности:')
        for row in results:
            print(f'ID:{row[0]} - {row[1]} ')
        cur.execute('''select * from Departments''')
        results = cur.fetchall()
        print('Факультеты')
        for row in results:
            print(f'ID:{row[0]} - {row[1]} ')
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

        cur.execute('''select
                Students.StuID,
                Students.Name,
                Majors.Name,
                Departments.Name
            from
                Students, Majors, Departments
            where
                Students.MajorID == Majors.MajorID and
                Students.DepID == Departments.DepID and
                Students.Name like ?''', (name,))
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]} - {row[1]} - {row[2]} - {row[3]}')
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            return len(results)


def update_row(id, majid, depid):
    conn = None
    try:
        conn = sqlite3.connect(DATA)
        cur = conn.cursor()
        cur.execute('''update Students
        MajorID = ?,
        DepID = ?
        where StuID == ?''', (majid, depid, id))
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
        cur.execute('''delete from Students
        where StuID == ?''', (id,))
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