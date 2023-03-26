import sqlite3

def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    cur.execute('select avg(RetailPrice) from Products')
    avg = cur.fetchone()[0]
    print(f'Средняя цена: {avg:.1f}')

    cur.execute('select min(RetailPrice) from Products')
    mine = cur.fetchone()[0]
    print(f'Минимальная цена: {mine}')

    cur.execute('select max(RetailPrice) from Products')
    maxi = cur.fetchone()[0]
    print(f'Максимальная цена: {maxi}')

    cur.execute('select sum(RetailPrice) from Products')
    sumi = cur.fetchone()[0]
    print(f'Сумма всех цен: {sumi}')




if __name__ == '__main__':
    main()