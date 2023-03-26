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
            pass
        elif vibor_polzovatel == '2':
            dice()
        elif vibor_polzovatel == '3':
            pass


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
def gen_max_count(digit, d1, d2, d3, d4, d5):
    count = 0
    if digit == d1:
        count += 1
    if digit == d2:
        count += 1
    if digit == d3:
        count += 1
    if digit == d4:
        count += 1
    if digit == d5:
        count +=1
def getRuletka():
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    k = 0
    count = randint(10, 20)
    for i in range(count):
        d1 = randint(0, 9)
        d2 = randint(0, 9)
        d3 = randint(0, 9)
        d4 = randint(0, 9)
        d5 = randint(0, 9)
        print('♥' * 10)
        print(f'{d1} {d2} {d3} {d4} {d5}')


        time.sleep(0.05)
    if d1 == d2 and d2 == d3 and d3 == d4 and d4 == d5:
        k = 10


def ruletka():
    global money
    while True:
        colorLine(3, 'Добро пожаловать на игру в ОДНОРУКОГО БАНДИТА!')
        color(14)
        print(f'\n У тебя на счету {money} рублей\n')
        color(5)
        print('1. При совпадении 2-х чисел ставка не списывается.')
        print('2. При совпадении 3-х чисел выигрыш 2:1.')
        print('3. При совпадении 4-х чисел выигрыш 5:1.')
        print('4. При совпадении 5-х чисел выигрыш 10:1.')
        print('0. Ставка 0 для выхода в главное меню\n.')
        stavka = getIntInput(0, 1000, 'Сделайте ставку: ' )


        if stavka == 0:
            return 0
        money -= stavka
        if stavka <= 0:
            print('У тебя нету денег, Бомжара боже')
            break

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
