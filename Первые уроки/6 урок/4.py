password="azimov"
print("Веддите пароль")
user_pas=input()
login="user"
print("Введите логин")
user_log=input()
c=(password==user_pas) and (login==user_log)
print(c)