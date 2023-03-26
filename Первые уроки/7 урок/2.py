price=67
cash=int(input("Введите сколько денег у вас в кошельке"))
num_kg=int(input("Сколько кг апельсинов вы собираетесь купить?"))
money=price*num_kg
dengi=cash-money
print(num_kg , "kg Апельсинов вам выйдет в", money ,"Рублей")
print("У вас в кошельке останется", dengi,"Рублей")