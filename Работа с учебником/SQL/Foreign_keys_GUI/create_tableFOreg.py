import sqlite3

def main():
    conn = sqlite3.connect('employees.db')

    cur = conn.cursor()
    cur.execute('pragma foreign_keys=ON')

    cur.execute('''create table Departments (DepartmentsID integer primary key not null,
     DepartmentsName text)''')
    cur.execute('''create table Locations (LocationID integer primary key not null,
    City text)''')

    cur.execute('''create table Employees (
    EmployeesID integer primary key not null,
    Name text,
    Position text,
    DepartmentID integer,
    LocationID integer,
    foreign key (DepartmentID) references
    Departments(DepartmentsID),
    foreign key (LocationID) references
    Locations (LocationID))''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()