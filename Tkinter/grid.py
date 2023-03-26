# from tkinter import *
#
# window = Tk()
# window.config(width=500,height=500)
#
# btn = Button(text='Первый текст')
# btn.pack()
# btn.config(state=NORMAL,text='Второй текст')
#
#
#
#
# window.mainloop()

from tkinter import *

window = Tk()
window.title('Калькулятор')
window.minsize(width=250, height=250)
# window.config(width=500,height=500)
for i in range(4):
    window.columnconfigure(index=i, weight=1)
for i in range(3):
    window.rowconfigure(index=i, weight=1)


button_text = ['CE', '%', '**', '*', '<',
               '7', '8', '9', '/', '',
               '4', '5', '6', '-', '',
               '1', '2', '3', '+', '',
               '.', '0', 'π', '=', '']

def calc(x):
    if x == 'CE':
        text = ''
        lab['text'] = text
        label['text'] = text

    elif x == '=':
        text = label['text']
        equals = eval(text)
        lab['text'] = f'{text}'
        label['text'] = f'{equals}'
    elif x == 'π':
        text = label['text']
        equals = eval(f'{text}*3.14')
        label['text'] = f'{equals}'
    elif x == '<':
        text = label['text']
        label['text'] = text[:-1]

    else:
        label['text'] += x



label = Label(text='', font=('Arial', 15))
label.grid(row=0, column=0, columnspan=4, sticky=NSEW)

lab = Label(text='', font=('Arial', 9))
lab.grid(row=1, column=1, columnspan=4, sticky=NSEW)

r = 2
c = 0
for i in button_text:
    Button(window, text=i, command=lambda x=i: calc(x), font='Arial', ).grid(row=r, column=c, sticky=NSEW)
    c += 1
    if c > 4:
        c = 0
        r += 1







window.mainloop()
























