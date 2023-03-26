print("Что ты взял из корзины?Там могут лежать:банан,апельсин,огурец,помидор.")
fruit=int(input("Это фрукт? 1-да 0-нет"))
if fruit==0:
    fruit=int(input("Продолговатый?1-да 0-нет"))
    if fruit==1:
        print("Огурец!")
    else:
        print("Помидор!")
if fruit==1:
    fruit=int(input("Круглый?1-да 0-нет"))
    if fruit==1:
        print("Апельсин!")
    else:
        print("Банан")