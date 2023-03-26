#
# def hello(name):
#     print(f'Hello,{name}')
#
# hello(input('Введите ваше имя:'))
#
# def f1(x,y):
#     print(x-y)
# f1(5,10)

#============================ФУНКЦИЯ
# def summa(x,y):
#     x + y
# print(summa(5,10))
#
# def summa(x,y):
#    return x + y
# print(summa(5,10)-10)
#
# import random
# def getDice():
#     count = random.randint (3, 8)
#     sleep = 0
#     while (count > 0):
#         x = random.randint(1, 6)
#         y = random.randint(1, 6)
#         print(' ' * 10, ' ---- ----')
#         print(' ' * 10, f'|{x}| |{y}|')
#         print(' ' * 10, ' ---- ----')
#         sleep += 1
#         count -= 1
#     return x + y

# def a():
#     return 5+5
#
#
# print(a()+5)
# def w():
#     b=5+5
#
# print(w()+5)
#
# def prodavec(summa):
#     pokupka1=500
#     pokupka2=300
#     stoimost=pokupka1+pokupka2
#     return 1000-stoimost
# print(prodavec()+10)
from random import randint
from time import sleep

def kubiki():
    count=randint(2,5)
    sleep1=0
    while(count>0):
        x=randint(1,6)
        y=randint(1,6)
        print(' ' * 10, ' ---- ----')
        print(' ' * 10, f'|{x}| |{y}|')
        print(' ' * 10, ' ---- ----')
        sleep(sleep1)
        sleep1+=1
        count-=1
    return x+y
print(kubiki())



