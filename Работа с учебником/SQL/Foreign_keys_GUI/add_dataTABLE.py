import sqlite3

def main():
    conn = sqlite3.connect('employees.db')

    name = input('Имя: ')
    position = input('Позиция: ')
    name = input('Имя: ')
    name = input('Имя: ')
    name = input('Имя: ')

    cur = conn.cursor()
    cur.execute('pragma foreign_keys=ON')

    cur.execute('''insert into Locations (City)
    values ("Сан-Хосе")''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()