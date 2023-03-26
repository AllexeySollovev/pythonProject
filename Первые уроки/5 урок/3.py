price_spagetti=110
price_cotleta=150
price_plombir=80
price_salat=100
price_tea=50
spagetti=int(input("Количество спагетти: "))
cotleta=int(input("Количество котлет:"))
plombir=int(input("Количество мороженого: "))
salat=int(input("Количество салата: "))
tea=int(input("Количество чая: "))
print()
print('Ваш заказ:')
print("Количество спагетти: ",spagetti)
print("Количество котлет: ",cotleta)
print("Количество мороженого: ",plombir)
print("Количество салата: ",salat)
print("Количество чая: ",tea)
print()
print("Стоимость вашей покупки:",price_spagetti*spagetti+price_cotleta*cotleta+price_plombir*plombir+price_salat*salat+price_tea*tea)