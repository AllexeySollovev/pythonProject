from ctypes import *
from time import sleep
from random import randint
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

money = 1000
playGame = True
def main():
    global playGame
    global money
    while playGame and money > 0:
        colorLine(1, '''
                               -Дарова, ты попал в самое опасное казино,
                               -Будь готов ко всем испытаниям
                             ''')
        print()
        color(1)
        print('•' * 30)
        color(3)
        print(f'\nУ тебя на счету {money} рублей\n')
        color(1)
        print('•' * 30)
        color(12)
        print('\nТы можешь сыграть:')
        print('1. Рулетка (Рекомендованная)')
        print('2. Кости')
        print('3. Однорукий бандит')
        print('0. Выход')


        choose = getIntInput(0, 3, 'Введите номер игры: ')
        if choose == 0:
            print('Жаль, что ты покидаешь нас. Удачи')
            sleep(3)
            playGame = False

        if choose == 1:
            color(12)
            print('♦' * 30)
            color(2)
            stavka = getIntInput(50, 300, 'Впишите вашу ставку(мин 50,макс 300): ')
            money -= stavka
            cubes = getIntInput(1, 36, 'Выбери число от 1 до 36: ')
            pick = randint(1, 36)
            if cubes == pick:
                print('Вы победили!')
                money += stavka * 2
            else:
                print(f'Выпало число {pick}, Ваша ставка не зашла')
        if choose == 2:
            dice()


def ruletka():
    pass


def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)


def colorLine(c,s):
    color(c)
    print(' ' * 25, '♠' * 50)
    print(' ' * 28, f'{s}')
    print(' ' * 25, '♠' * 50)

def getIntInput(minimum,maximum,message):
    ret = -1
    while ret < minimum or ret > maximum:
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
           print('Вы ввели буквенное выражение, заместо цифренного')
    return ret

def getdise():
    global money
    sleep1 = 0
    povorot = randint(3,8)
    for i in range(povorot):
        x = randint(1,6)
        y = randint(1,6)
        print(10 * '','--- ---',10 * '')
        print(10 * '', f'|{x}| |{y}|', 10 * '')
        print(10 * '', '--- ---', 10 * '')
        sleep(sleep1)
        sleep1 += 1/(i+1)
        return x+y

def dice():
    global money
    colorLine(12,'Добро пожаловать в игру кости!')
    while True:
        print(f'Ваш баланс:{money} рублей')
        choose = getIntInput(0,1,'0-Выйти из игры, 1-Продолжить:  ')
        if choose == 0:
            break
        stavka =  getIntInput(0,1000,'Сделайте ставку от 1 до 1к: ')
        if stavka == 0:
            return 0
        if stavka > money:
            stavka = money
        result = getdise()
        win = False
        for i in range(3):
            print(f'На кубиках выпало {result} очков')
            choose2 = getIntInput(0,3,'0 - Выход,\n1 - Выпадет число больше,\n2 - Выпадет число меньше,\n3 - Число будет равно ')
            if choose2 == 0 or money < stavka:
                money -= stavka
                break

            else:
                k = 1
                last_result = getdise()
                if last_result > result:
                    if choose2 == 1:
                        win = True
                elif last_result < result:
                    if  choose2 == 2:
                        win = True
                elif last_result == result:
                    if choose2 == 3:
                        win = True
                        k = 2
            if win:
                money += stavka / 5 * k
                pobeda(stavka / 5 * k)
            else:
                money -= stavka
                lose(stavka)
            result = last_result
def pobeda(money_win):
    global money
    color(3)
    print(f'Поздравляю! Твоя ставка сыграла, Ты выиграл {money_win} рублей.\n Твой баланс {money} рублей')
def lose(money_lose):
    global money
    color(3)
    print(f'К сожалению твоя ставка не сыграла!)Ты проиграл {money_lose} рублей.\n Твой баланс {money} рублей')




main()