import sqlite3

def main():
    conn = sqlite3.connect('company.db')

    cur = conn.cursor()

    cur.execute('''create table if not exists FloatTable (CustomerID real primary key not null,
    Name text,
    Email text)''')

    cur.execute('''create table if not exists Employees (EmployeeID integer primary key not null,
        Name text,
        Postition text)''')

    # cur.execute('drop table Customers')  - Удаление таблицы

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()