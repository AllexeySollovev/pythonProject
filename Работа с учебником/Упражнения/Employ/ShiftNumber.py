from employ import ProductionWorker

print('---Заполните данные для устраивания на работу---')
name = input('Введите ваше имя: ')
phone = int(input('Введите ваш номер телефона: '))
snumber = float(input('Введите смену в которой вам удобнее будет работать\n'
                '(1 - Дневная 2 - ночная): '))
rate = float(input('Введите желаемую почасовую ставку: '))

employee = ProductionWorker(name, phone, snumber, rate)
print('Введенные вами данные\n'
      '=====================================================')
print(f'Ваше имя: {employee.get_name()}\n'
      f'Ваш номер телефона: {employee.get_phone()}\n'
      f'Ваша смена: {employee.get_shiftnumber()}\n'
      f'Ваша почасовая ставка: {employee.get_rate()}')
print('======================================================')