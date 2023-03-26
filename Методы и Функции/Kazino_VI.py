from ctypes import *
import time
from random import randint

windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

money = 1000
playGame = True


# Главный метод для запуска игры
def main():
    global playGame
    while (playGame and money > 0):
        colorLine(3, '''Приветствую, игрок! Ты попал в игру "Казино".\n 
                                Ты можешь выбрать одну из трех игр!''')
        color(12)
        print('\nТы можешь сыграть в: ')
        print('1. Рулетку')
        print('2. Кости')
        print('3. Однорукого бандита')
        print('0. Выход.\n')

        vibor_polzovatel = getInput('0, 1, 2, 3', 'Выберите пункт меню: 0, 1, 2, 3: ')

        if vibor_polzovatel == '0':
            print('Жаль, что ты покидаешь игру. Возвращайся скорей!')
            time.sleep(1)
            playGame = False
        elif vibor_polzovatel == '1':
            roulete()
        elif vibor_polzovatel == '2':
            dice()
        elif vibor_polzovatel == '3':
            one_hand_bandit()


def roulrange():
    count = randint(15,30)
    sektor = 0
    for i in range(count):
        sektor = randint(1,36)
        print(' ' * 10, '♣' * 6)
        print(' ' * 10, f'  {sektor}   ')
        print(' ' * 10, '♣' * 6)
    return sektor



def RedAndBlack():
    count = randint(15,30)
    sektor = 0
    for i in range(count):
        sektor = randint(0,1)
        if sektor == 0:
            print(' ' * 10, '♣' * 6)
            print(' ' * 10, 'Красный')
            print(' ' * 10, '♣' * 6)
        else:
            print(' ' * 10, '♣' * 5)
            print(' ' * 10, 'Чёрный')
            print(' ' * 10, '♣' * 5)
        time.sleep(1 / ( count - i))
    return sektor

def roulete():
    global money
    while True:
        colorLine(4, "Добро пожаловать в рулетку")
        stavka = getIntInput(0, money, "Сделайте ставку: ")
        if stavka == 0:
            return 0
        money -= stavka
        choose = getIntInput(1, 3, 'Выберите режим игры:\n1 - Красное/Чёрное,\n2 - Диапазон(1 - 18,19 - 36)\n'
'3 - Конкретное число,\n0 - Выход: ')

        if choose == 0:
            money += stavka
            print('Пока,Пока!')
            break
        elif choose == 1:
            pick = int(input('0 - Красный . 1 - черный: '))
            sektor = RedAndBlack()
            if pick == sektor:
                money += stavka * 1.25
                pobeda(stavka * 1.25)
            else:
                proigr(stavka)
        elif choose == 2:
            pick = int(input('0 - (1 - 18), 1 - (19 - 36): '))
            sektor = roulrange()
            if (i <= sektor <= 18 and pick == 0) or (19 <= sektor <= 36 and pick == 1):
                money += stavka * 1.5
                pobeda(stavka * 1.5)
            else:
                proigr(stavka)
        elif choose == 3:
            pick = getIntInput(1,36, 'Число от 1 до 36: ')
            sektor = roulrange()
            if sektor == NumberI():
                money += stavka * 10
                pobeda(stavka * 10)
            else:
                proigr(stavka)







def getWin(number, d1, d2, d3, d4, d5):
    count = 0
    if number == d1:
        count += 1
    if number == d2:
        count += 1
    if number == d3:
        count += 1
    if number == d4:
        count += 1
    if number == d5:
        count += 1
    return count


def get_one_hand_bandit():
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    count = randint(10, 20)
    for i in range(count):
        d1 = randint(0, 9)
        d2 = randint(0, 9)
        d3 = randint(0, 9)
        d4 = randint(0, 9)
        d5 = randint(0, 9)
        print(" " * 10, "*" * 11)
        print(" " * 10, f"{d1} {d2} {d3} {d4} {d5}")
        print(" " * 10, "*" * 11)
    counts = []
    counts.append(getWin(d1, d1, d2, d3, d4, d5))
    counts.append(getWin(d2, d1, d2, d3, d4, d5))
    counts.append(getWin(d3, d1, d2, d3, d4, d5))
    counts.append(getWin(d4, d1, d2, d3, d4, d5))
    counts.append(getWin(d5, d1, d2, d3, d4, d5))
    MaxCount = max(counts)
    return MaxCount


def one_hand_bandit():
    global money
    while True:
        colorLine(4, "Добро пожаловать в игру Однорукий бандит.")
        choose = int(input("0 - Выход, 1 - Играть: "))
        if choose == 0:
            break
        stavka = getIntInput(0, money, "Сделайте ставку: ")
        money -= stavka
        MaxCount = get_one_hand_bandit()
        if MaxCount == 1:
            proigr(stavka)
        elif MaxCount == 2:
            money += stavka
            print("Ты ничего не выиграл и не проиграл")
        elif MaxCount == 3:
            money += stavka * 2
            pobeda(stavka * 2)
        elif MaxCount == 4:
            money += stavka * 5
            pobeda(stavka * 5)
        elif MaxCount == 5:
            money += stavka * 10
            pobeda(stavka * 10)


# Анимация броска костей (родитель dice())
def getDice():
    count = randint(3, 4)
    sleep = 0
    while (count > 0):
        color(count + 7)
        x = randint(1, 6)
        y = randint(1, 6)
        print(' ' * 10, '  ---     ---')
        print(' ' * 10, f' | {x} |   | {y} |')
        print(' ' * 10, '  ---     ---')
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
    return x + y


# Метод для мини-игры "Кости"
def dice():
    global money
    playGame = True
    while (playGame and money > 0):
        print()
        colorLine(10, '    Добро пожаловать на игру в КОСТИ!')
        color(14)
        print(f'Имейте ввиду, у Вас всего {money} рублей.\n')
        color(7)
        stavka_igroka = getIntInput(0, 1000, '''Сколько денег достать из кошелька, чтобы поиграть в кости? ''')
        if (stavka_igroka == 0):
            return 0

        playRound = True
        control = stavka_igroka
        Result = getDice()

        while (playRound and stavka_igroka > 0 and money > 0):
            if (stavka_igroka > money):
                stavka_igroka = money
            color(11)
            print(f'\nВы решили поставить {control} рублей.')
            color(7)
            print(f'\nТекущая сумма чисел на костях равняется {Result}.\n')
            color(11)

            prognoz = getInput('0123', '''Как считаете, следующая сумма граней будет: 
                                 1 - больше, 2 - меньше, 3 - равна или 0 - выход: ''')
            if (prognoz != '0'):
                money -= stavka_igroka
                diceResult = getDice()
                win = False
                if (Result > diceResult):
                    if (prognoz == '2'):
                        win = True
                elif (Result < diceResult):
                    if (prognoz == '1'):
                        win = True
                elif (Result == diceResult):
                    if (prognoz == '3'):
                        win = True
                else:
                    stavka_igroka = control
                    proigr(stavka_igroka)
                Result = diceResult

                if (win):
                    money += stavka_igroka + stavka_igroka // 5
                    pobeda(stavka_igroka // 5)
                    stavka_igroka += stavka_igroka // 5
                else:
                    stavka_igroka = control
                    proigr(stavka_igroka)
                    if money <= 0:
                        print('Сожалеем, но без денег, Вам нечего делать в Казино. Пшел вон!')
                        time.sleep(2)
                        playGame = False
            else:
                money -= stavka_igroka
                playRound = False


# Установка цвета текста
def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)


# Вывод на экран цветного приветствия игрока, обрамленного звездочками
def colorLine(c, s):
    color(c)
    print(' ' * 25, '*' * 50)
    print(' ' * 28, f'{s}')
    print(' ' * 25, '*' * 50)


# Функция для выбора пунктов из меню
def getInput(digit, message):
    color(11)
    ret = ''
    while (ret == '' or not ret in digit):
        ret = input(message)
    return ret


# Минимальное и максимальное значение ставки
def getIntInput(minimum, maximum, message):
    ret = -1
    while (ret < minimum or ret > maximum):
        st = input(message)
        if (st.isdigit()):
            ret = int(st)
        else:
            print('Введите корректное число!')
    return ret


# Вывод сообщения о выигрыше
def pobeda(result):
    color(14)
    print(f'''Победа за тобой! Ты выиграл {result} рублей.
    Всего в кошельке у тебя осталось: {money}''')


# Вывод сообщения о проигрыше
def proigr(result):
    color(12)
    print(f'''Ты проиграл! Ты потерял {result} рублей.
    Всего в кошельке у тебя осталось: {money}''')


main()
