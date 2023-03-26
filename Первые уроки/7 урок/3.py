price=int(input("Введите цену на 1 кг апельсинов: "))
num_kg=int(input("Введите сколько вам нужно кг: "))
cash=int(input("Сколько денег у Вас в кошельке: "))
amount=price*num_kg
print("За", num_kg, "кг апельсин нужно заплетить", amount,"рублей")
dif=cash-amount
#print("У Вас останется", dif,"рублей")
if dif>0:
    print("Покупаем!")
if dif<0:
    print("Давай возьмем поменьше, у нас нет денег!")
if dif==0:
    print("Ух! Едва хватило денег!")
