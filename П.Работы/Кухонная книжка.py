from ctypes import *
import time
print('Привет! Ты попал в книжку с разными ингредиентами. ')
print('Ты можешь ввести свои ингредиенты и он найдет рецепт, ты можешь ввести рецепт, и он введет ингредиенты')

def sostav():
    while True:
        coct = input('Введи ингредиент, которые у тебя есть: ')
        borsh = ['свёкла','морковь','картофель','говядина','свинина']
        omelet = ['яйцо']
        borsh.extend(omelet)

        for i in borsh:
            if coct == i:
                print(f'Вы можете приготовить Борщ: ')
            time.sleep(3)
        next = int(input('Хотите добавить 2 ингредиент, или выйти?\n0 - Выйти\n'
                     '1 - Продолжить'))
        if next == 0:
            break
        else:

            coct2 = input('Введите 2 ингредиент: ')
            if i == coct and coct2:
                print(f'')



sostav()