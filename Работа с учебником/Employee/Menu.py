from employee import Employee
from pickle import dump, load
def main():

    dict_e = load_employee()
    choice = 0
    while choice != 5:
        choice = get_choice()
        if choice == 1:
            look(dict_e)
        elif choice == 2:
            add(dict_e)
        elif choice == 3:
            change(dict_e)
        elif choice == 4:
            delete(dict_e)
    save_employees(dict_e)
def load_employee():
    with open('data.dat', 'rb')as file:
        dict_e = load(file)

        return dict_e
def get_choice():
    print('В меню разработчика, вы можете:\n'
          '1 - Найти сотрудника\n'
          '2 - Добавить сотрудника\n'
          '3 - Изменить данные о сотруднике\n'
          '4 - Удалить сотрудника из БД\n'
          '5 - Выйти из меню разработчика\n')
    choice = int(input('Ваш выбор: '))

    return choice
def look(dict_e):
        name = input('\nВведите имя сотрудника\n'
                     '>: ')
        print('\n')
        print(dict_e.get(name, 'Данное имя не присутствует в БД'))
def add(dict_e):
    name = input('\nВведите имя сотрудника\n'
                 '>:')
    ident = input('Введите Идентификатор сотрудника\n'
                  '>:')
    section = input('Введите отдел сотрудника\n'
                    '>:')
    post = input('Введите должность сотрудника\n'
                 '>: ')
    employee = Employee(name, ident, section, post)
    if name not in dict_e:
        dict_e[name] = employee
        print('Сотрудник добавлен в БД\n')
    else:
        print('Имя сотрудника уже использовано в БД\n')
def change(dict_e):
    name = input('Введите имя сотрудника\n'
                 '>:')
    if name in dict_e:
        ident = input('Введите новый идентификатор сотрудника\n'
                      '>:')
        section = input('Введите новый отдел сотрудника\n'
                        '>:')
        post = input('Введите новую должность сотрудника\n'
                     '>: ')
        employee = Employee(name, ident, section, post)
        dict_e[name] = employee
        print('Данные изменены\n')
    else:
        print('Данное имя сотрудника было не найдено в БД\n')
def delete(dict_e):
    name = input('Введите имя сотрудника которое нужно удалить\n'
                 '>: ')
    if name in dict_e:
        del dict_e[name]
        print('Данные о сотруднике удалены\n')
    else:
        print('Данные о сотруднике были не найдены\n')
def save_employees(dict_e):
    with open('data.dat', 'wb')as file:
        dump(dict_e, file)
if __name__ == '__main__':
    main()