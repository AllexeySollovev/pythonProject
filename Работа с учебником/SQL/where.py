import sqlite3

def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    min_price = float(input('Введите минимальную цену:'))

    cur.execute('''select Description, RetailPrice from Products
                                where RetailPrice >= ?''',
                (min_price,))

    results = cur.fetchall()

    if len(results) > 0:
        print('Товар                                Цена')
        for row in results:

            print(f'{row[0]:35} {row[1]:>5}')
    else:
        print('По указанным параметрам ничего не найдено!')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()