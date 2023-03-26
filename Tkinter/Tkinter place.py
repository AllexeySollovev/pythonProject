from tkinter import *


def b1c():
    if bc[0] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn1.config(text='0', fg=fg1)
        bc[0] = 0

    else:
        btn1.config(text='X', fg=fg)
        bc[0] = 1
        game_cond(bc)


def b2c():
    if bc[1] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn2.config(text='0', fg=fg1)
        bc[1] = 0
    else:
        btn2.config(text='X', fg=fg)
        bc[1] = 1
        game_cond(bc)


def b3c():
    if bc[2] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn3.config(text='0', fg=fg1)
        bc[2] = 0
    else:
        btn3.config(text='X', fg=fg)
        bc[2] = 1
        game_cond(bc)


def b4c():
    if bc[3] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn4.config(text='0', fg=fg1)
        bc[3] = 0
    else:
        btn4.config(text='X', fg=fg)
        bc[3] = 1
        game_cond(bc)


def b5c():
    if bc[4] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn5.config(text='0', fg=fg1)
        bc[4] = 0
    else:
        btn5.config(text='X', fg=fg)
        bc[4] = 1
        game_cond(bc)


def b6c():
    if bc[5] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn6.config(text='0', fg=fg1)
        bc[5] = 0
    else:
        btn6.config(text='X', fg=fg)
        bc[5] = 1
        game_cond(bc)


def b7c():
    if bc[6] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn7.config(text='0', fg=fg1)
        bc[6] = 0
    else:
        btn7.config(text='X', fg=fg)
        bc[6] = 1
        game_cond(bc)


def b8c():
    if bc[7] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn8.config(text='0', fg=fg1)
        bc[7] = 0
    else:
        btn8.config(text='X', fg=fg)
        bc[7] = 1
        game_cond(bc)


def b9c():
    if bc[8] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        btn9.config(text='0', fg=fg1)
        bc[8] = 0
    else:
        btn9.config(text='X', fg=fg)
        bc[8] = 1
        game_cond(bc)

button_font = ('Arial', 90)
fg = ('Blue')
fg1 = ('Red')
# if bc[0] == bc[1] == bc[2] == 0 or \
#         bc[3] == bc[4] == bc[5] == 0 or \
#         bc[6] == bc[7] == bc[8] == 0 or \
#         bc[0] == bc[3] == bc[6] == 0 or \
#         bc[1] == bc[4] == bc[7] == 0 or \
#         bc[2] == bc[5] == bc[8] == 0 or \
#         bc[0] == bc[4] == bc[8] == 0 or \
#         bc[2] == bc[4] == bc[6] == 0:
#     text = 'Победил 1 игрок'
# elif bc[0] == bc[1] == bc[2] == 1 or \
#         bc[3] == bc[4] == bc[5] == 1 or \
#         bc[6] == bc[7] == bc[8] == 1 or \
#         bc[0] == bc[3] == bc[6] == 1 or \
#         bc[1] == bc[4] == bc[7] == 1 or \
#         bc[2] == bc[5] == bc[8] == 1 or \
#         bc[0] == bc[4] == bc[8] == 1 or \
#         bc[2] == bc[4] == bc[6] == 1:
#     text = 'Победил 2 игрок'
def game_cond(ist):
    if bc[0] == bc[1] == bc[2] == 0 or \
            bc[3] == bc[4] == bc[5] == 0 or \
            bc[6] == bc[7] == bc[8] == 0 or \
            bc[0] == bc[3] == bc[6] == 0 or \
            bc[1] == bc[4] == bc[7] == 0 or \
            bc[2] == bc[5] == bc[8] == 0 or \
            bc[0] == bc[4] == bc[8] == 0 or \
            bc[2] == bc[4] == bc[6] == 0:
        text = 'Победил 1 игрок'
    if bc[0] == bc[1] == bc[2] == 1 or \
            bc[3] == bc[4] == bc[5] == 1 or \
            bc[6] == bc[7] == bc[8] == 1 or \
            bc[0] == bc[3] == bc[6] == 1 or \
            bc[1] == bc[4] == bc[7] == 1 or \
            bc[2] == bc[5] == bc[8] == 1 or \
            bc[0] == bc[4] == bc[8] == 1 or \
            bc[2] == bc[4] == bc[6] == 1:
        text = 'Победил 2 игрок'
    elif count == 9:
        text = 'Ничья'

    else:
        text = 'Идёт игра!'
    game_text.config(text=text)




count = 0
bc = [-1] * 9

window = Tk()
window.title('Крестики-нолики')
window.config(width=500, height=500)  # задали размер окна
game_text = Label(window, text='Начинаем игру!')
# game_text.place(x=234,y=50,anchor=CENTER)
game_text.place(relx=0.5, rely=0.05, anchor=CENTER)

btn1 = Button(window, text='', command=b1c, font=button_font)
btn2 = Button(window, text='', command=b2c, font=button_font)
btn3 = Button(window, text='', command=b3c, font=button_font)
btn4 = Button(window, text='', command=b4c, font=button_font)
btn5 = Button(window, text='', command=b5c, font=button_font)
btn6 = Button(window, text='', command=b6c, font=button_font)
btn7 = Button(window, text='', command=b7c, font=button_font)
btn8 = Button(window, text='', command=b8c, font=button_font)
btn9 = Button(window, text='', command=b9c, font=button_font)

btn1.place(height=100, width=100, x=100, y=100)
btn2.place(height=100, width=100, x=200, y=100)
btn3.place(height=100, width=100, x=300, y=100)

btn4.place(height=100, width=100, x=100, y=200)
btn5.place(height=100, width=100, x=200, y=200)
btn6.place(height=100, width=100, x=300, y=200)

btn7.place(height=100, width=100, x=100, y=300)
btn8.place(height=100, width=100, x=200, y=300)
btn9.place(height=100, width=100, x=300, y=300)
window.mainloop()
