import sqlite3

def main():
    again = 'д'

    while (again == 'д'):
        try:
            id_item = int(input('Введите ID:'))
            name_item = input('Введите название:')
            cost_item = float(input('Введите стоимость:'))

            add_item(id_item, name_item, cost_item)
        except ValueError:
            print('Error 404')

        again = input('Хотите добавить еще товаров?(д\н)\n'
                      '>:')

def add_item(idi, name, cost):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')

        cur = conn.cursor()

        cur.execute('''insert into Inventory (ItemID, ItemName, Price)
        values (?, ?, ?)''',
                    (idi, name, cost))
        conn.commit()
    except sqlite3.Error as err:
        print('ОШИБКА!!!', err)
    finally:
        if conn != None:
            conn.close()

if __name__ == '__main__':
    main()
