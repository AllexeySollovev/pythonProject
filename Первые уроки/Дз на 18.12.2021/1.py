bal=int(input("Введи свой балл за тест: "))
if bal>=90 and bal<=100:
    print("У вас 5")
elif bal>=70 and bal<90:
    print("У вас 4")
elif bal>=50 and bal<70:
    print("У вас 3")
elif bal>=0 and bal<50:
    print("Приходите на пересдачу!")
else:
    print("Вы ввели неверное число!")
