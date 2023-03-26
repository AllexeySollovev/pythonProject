import sqlite3

def main():
    again = 'д'

    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    cur.execute('''create table if not exists Products (ProductID integer primary key not null,
    Description text,
    UnitCost real,
    RetailPrice real,
    UnitsOnHand integer)''')

    while again == 'д':
        name = input('Название:')
        unitcost = float(input('Цена за 1шт:'))
        retailcost = float(input('Розничная цена:'))
        onhand = int(input('Осталось шт:'))


        cur.execute('''insert into Products (Description, UnitCost, RetailPrice, UnitsOnHand)
        values (?, ?, ?, ?)''',
                    (name, unitcost, retailcost, onhand))

        again = input('Добавить еще одну позицию(н/д):')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()