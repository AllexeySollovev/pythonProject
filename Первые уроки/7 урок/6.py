height=float(input("Введите свой рост: "))
if height>1.05 and height<2:
    print("Проходите")
elif height>0.9:
    print("Только в сопроводжении родителей!")
elif height<0.9 or height>2:
    print("Вы не подходите по росту")
