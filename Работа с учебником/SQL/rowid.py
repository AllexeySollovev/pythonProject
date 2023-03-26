import sqlite3

def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    cur.execute('select RowID from Products')
    idp = cur.fetchall()
    print(idp)

if __name__ == '__main__':
    main()
