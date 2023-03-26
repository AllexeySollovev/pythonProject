from employee import Employee
from pickle import dump, load
from time import sleep
def main():
    employees = {}
    print('Введите данные о 3 сотрудниках!')
    sleep(5)
    for employee in range(1, 4):
        name = input('Введите имя сотрудника')
        identification = input('Введите Id номер сотрудника: ')
        section = input('Введите Отдел сотрудника: ')
        post = input('Введите должность сотрудника: ')
        employees['empl' + str(employee)] = Employee(name, identification, section, post)
        print('\n')
        sleep(2)
    write_employee(employees)
    print('Данные о всех сотрудниках: ')
    sleep(3)
    dict_employees = load_employee()
    list_employee(dict_employees)




def list_employee(dicte):
    for key in dicte:
        print(dicte[key])
    print('\n')

def load_employee():
    try:
        with open('data.dat', 'rb')as file:
            employee = load(file)
    except IOError and EOFError:
            employee = {}
    return employee
def write_employee(employee):
    with open('data.dat', 'wb')as file:
        dump(employee, file)
if __name__ == '__main__':
    main()