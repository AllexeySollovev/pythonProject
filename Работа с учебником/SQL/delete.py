import sqlite3

def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    idp = int(input('Введите ID: '))
    cur.execute('''select * from Products
    where ProductID == ?''', (idp,))
    results = cur.fetchone()

    if results != None:
        choice = input(f'Вы точно хотите удалить {results[0]}\n'
                       f'(д\н): ')
        if choice.lower() == 'д':
            cur.execute('''delete from Products
            where ProductID == ?''', (idp,))
            print('Продукт был удален!')
            conn.commit()
        else:
            print('Продукт не был удален!')
    else:
        print(f'Продукт под номером {idp} был не найден!')
    conn.close()

if __name__ == '__main__':
    main()