import sqlite3

def main():
    conn = sqlite3.connect('inventory.db')

    cur = conn.cursor()
    # Если после create table написать if not exists - создается таблица если она не существует
    cur.execute('''create table if not exists Inventory (ItemID integer primary key not null,
    ItemName text,
    Price real)''')

    cur.execute('''insert into Inventory (ItemName, Price)
    values ("Отвертка", 4.99)''')

    cur.execute('''insert into Inventory (ItemName, Price)
        values ("Молоток", 12.99)''')

    cur.execute('''insert into Inventory (ItemName, Price)
        values ("Плоскогубцы", 14.99)''')
    #or

    cur.execute('''insert into Inventory (ItemName, Price)
    values ("Отвертка", 4.99),
    ("Молоток", 12.99),
    ("Плоскогубцы", 14.99)''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()