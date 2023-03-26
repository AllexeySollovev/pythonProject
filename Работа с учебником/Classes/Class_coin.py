from tkinter import *
import random

class Coin:
    def __init__(self):
        self.side_up = 'Орёл'
    def toss(self):
        up = random.randint(0, 7)
        if up >= 0 and up < 3:
            self.side_up = 'Орёл'
        elif up >= 3 and up < 7:
            self.side_up = 'Решка'
        else:
            self.side_up = 'Боковая сторона'
    def  get_side_up(self):
        return self.side_up

count_coin = 0
Ist = ''
def main():

    coin = Coin()
    def ready():
        global Ist
        global count_coin
        coin.toss()
        label['text'] = f'{coin.get_side_up()}'
        Ist += f'{coin.get_side_up()}\n'
        count_coin += 1

    def window_value():
        indicators = Toplevel()
        indicators.geometry('200x500')

        parameter = Label(indicators, text=f'{count_coin} раз подброшено\n------------------\n'
                                           f'Результаты:\n{Ist}')
        parameter.pack()

    def window_chance():
        winchance = Toplevel()
        winchance.geometry('200x80')
        chance_coin = Label(winchance, text='Боковая сторона - 14%\n'
                                         'Решка - 42%\n'
                                         'Орёл - 42%')
        chance_coin.pack()




    window = Tk()
    window.geometry(f'300x300+{window.winfo_screenwidth() // 2 - 150}+{window.winfo_screenheight() // 2 - 150}')
    window.title('Coin')
    window.resizable(False, False)

    label = Label(window, text='Монетка', font='arial 15')
    btnready = Button(window, text='Бросить монетку', command=ready)
    values = Button(window, text='Показатели', command=window_value)
    chance = Button(window, text='Шансы', command=window_chance)


    label.place(x=110, y=35)
    btnready.place(x=10, y=150, width=280, height=40)
    values.place(x=20, y=265)
    chance.place(x=235, y=265)


    mainloop()





if __name__ == '__main__':
    main()

































