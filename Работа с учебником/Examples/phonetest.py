from cellphone import CellPhone

# man = input('Введите производителя: ')
# mod = input('Введите номер модели: ')
# retail = float(input('Введите розничную цену: '))
#
# phone = CellPhone(man, mod, retail)
# print(f'Производитель: {phone.get_manufact()}\n'
#       f'Номер модели: {phone.get_model()}\n'
#       f'Розничная цена: {phone.get_price()}')

def main():
        phones = make_list()

        print(f'Вот введеные вами данные:')
        display_list(phones)
def make_list():
      phone_list = []

      print('Введите данные о пяти телефонах')
      for count in range(1, 2):
            print('Номер телефона ', count)
            man = input('Введите производителя: ')
            mod = input('Введите номер модели: ')
            retail = float(input('Введите розничну цену: '))
            phone = CellPhone(man, mod, retail)

            phone_list.append(phone)
      return phone_list

def display_list(phone_list):
      for item in phone_list:
            print(item.get_manufact())
            print(item.get_model())
            print(item.get_price())

if __name__ == '__main__':
    main()