print("Привет,Я - умный калькулятор!")
a=int(input("Введи первое число: "))
b=int(input("Введи второе число: "))
op=input("Введите операцию(+ - * /):  ")
if op=="+":
    ans=a+b
elif op=="-":
    ans=a-b
elif op=="*":
    ans=a*b
elif op=="/":
    ans=a/b
else:
    print("В моей базе нету такой операции!")
print("Результат:",ans)