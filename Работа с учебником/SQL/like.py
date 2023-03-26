import sqlite3

def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()
    name = input('Введи:')
    name = f'%{name}%'

    cur.execute('''select * from products
    where Description like ?''', (name,))

    results = cur.fetchall()

    for row in results:
        print(row)

if __name__ == '__main__':
    main()