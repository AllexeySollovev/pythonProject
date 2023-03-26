import sqlite3

MAX_CHOICE = 5
MIN_CHOICE = 1
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

DATABASE = 'inventory.db'

def main():
    choice = 0
    while choice != 5:
        get_menu_choice()
        choice = get_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()

def get_menu_choice():
    print('\n----- Меню введения учета инструментов -----\n'
          '1. Добавить позицию\n'
          '2. Найти товар\n'
          '3. Обновить позицию\n'
          '4. Удалить позицию\n'
          '5. Выйти\n')

def get_choice():
    choice = int(input('Введите ваш выбор >'))

    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        choice = int(input('Введите ваш выбор >'))
    return choice

def create():
    name = input('Введите название позиции:')
    price = float(input('Введите цену позиции:'))
    insert_row(name, price)

def read():
    name = input('Введите название искомой позиции:')
    num_found = display_item(name)
    print(f'{num_found} строк найдено.')

def update():
    read()

    id_select = int(input('Введите ID позиции:'))
    name = input('Введите новое название позиции:')
    price = float(input('Введите новую цену позиции:'))
    num_updated = update_row(id_select, name, price)
    print(f'{num_updated} строк было обновлено.')

def delete():
    read()

    id_select = int(input('Введите ID позиции:'))

    num_delete = delete_row(id_select)
    print(f'{num_delete} строк было удалено.')


def insert_row(name, price):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute('''insert into Inventory (ItemName, Price)
        values (?, ?)''',
                    (name, price))
        conn.commit()
    except sqlite3.Error or ValueError as err:
        print('Ошибка в вводимых данных - ', err)

    finally:
        if conn != None:
            conn.close()
            print('Позиция добавлена!')

def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        name = f'%{name}%'
        cur.execute('''select * from Inventory
        where ItemName like ?''', (name,))
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]}| {row[1]} - {row[2]}р')
    except sqlite3.Error or ValueError as err:
        print('Ошибка в вводимых данных - ', err)
    finally:
        if conn != None:
            conn.close()
            return len(results)

def update_row(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute('''update Inventory
        set ItemName = ?, Price = ?
        where ItemID == ?''',
                    (name, price, id))

        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка вводимых данных - ', err)
    finally:
        if conn != None:
            conn.close()
        return num_updated

def delete_row(id):
    conn = None

    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute('''delete from Inventory
        where ItemID == ?''', (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка вводимых данных - ', err)
    finally:
        if conn != None:
            conn.close()
        return num_deleted


if __name__ == '__main__':
    main()

