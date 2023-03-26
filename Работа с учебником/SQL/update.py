import sqlite3
#
# def main():
#     conn = sqlite3.connect('chocolate.db')
#
#     cur = conn.cursor()
#
#     cur.execute('''update Products
#     set RetailPrice = 13.99
#     where Description == "Шоколадные трюфели"''')
#
#     conn.commit()
#     conn.close()
#
# if __name__ == '__main__':
#     main()


def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    idp = int(input('Введите ID продукта:'))

    cur.execute('''select * from Products
     where ProductID == ?''', (idp,))
    product = cur.fetchone()
    if product != None:
        print(f'Товар:{product[1]}\nСтоимость:{product[3]} - На складе:{product[4]}шт.')

        newretail = float(input('Введите новую розничную цену:'))
        newunits = int(input('Введите сколько товаров имеется:'))
        cur.execute('''update Products
        set RetailPrice = ?,
        UnitsOnHand = ?
        where ProductID == ?''', (newretail, newunits, idp))

    else:
        print(f'Номер {idp} был не найден!')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()