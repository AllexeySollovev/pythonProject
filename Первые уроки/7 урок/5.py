price=int(input("Введите цену на 1 кг апельсинов: "))
num_kg=int(input("Введите сколько вам нужно кг: "))
cash=int(input("Сколько денег у Вас в кошельке: "))
amount=price*num_kg
print("За", num_kg, "кг апельсин нужно заплатить", amount,"рублей")
dif=cash-amount
#print("У Вас останется", dif,"рублей")
if dif>0:
    print("Покупаем!")
elif dif==0:
    print("Едва хватило денег!")
else:
    print("Давай возьмем поменьше, у нас нет денег!")
