price = int(input("Введите цену подарка: "))
if price >= 500 and price <= 1000:
    print("Покупаем!")
if price < 500:
    print("Слишком дешевый!")
if price > 1000:
    print("Слишком дорогой!")
