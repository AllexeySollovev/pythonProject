print("Здравствуй,Пользователь.Авторизуйтесь пожалуйста")
b =input"babaika1999"
c =input'qwerty123'


while(True):
    a=input("Введите логин: ")
    if(a==b):
        print("Login has activated")
        y=input("Введите пароль: ")
        if(y==c):
            print("Вы успешно вошли!")
            break
        else:
            print("Вы допустили ошибку. попробуйте еще раз.")
    else:
        print("Вы допустили ошибку. попробуйте еще раз.")
input()