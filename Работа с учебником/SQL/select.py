import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    cur.execute('select * from Products')

    results = cur.fetchall()  # -Весь список or cur.fetchone() - 1 элемент

    for row in results:
            print(f'ID:{row[0]:3} {row[1]:35} {row[2]:5} {row[3]:7} (Осталось:{row[4]:5})')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
