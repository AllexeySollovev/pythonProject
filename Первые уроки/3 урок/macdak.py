price_hamburger=60
price_potatoes=85
price_cola=100
print('Давай сформируем заказ: ')
num_hamburger=int(input("Количество гамбургеров: "))
num_potatoes=int(input('Количество картошки: '))
num_cola=int(input("Количество колы: "))
cost=price_hamburger*num_hamburger+price_potatoes*num_potatoes+price_cola*num_cola
print('Ваш заказ:')
print("Гамбургер", num_hamburger, "шт")
print('Картошка фри',num_potatoes,'шт')
print('Кока-кола', num_cola,'шт')
print("Стоимость вашего заказа:",cost,'р')