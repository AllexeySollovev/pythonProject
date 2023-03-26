from tkinter import *
from random import randint
def random_number():
    fnum = int(entry_before.get())
    lnum = int(entry_after.get())
    number = randint(fnum, lnum)
    result['text'] = f'{number}'




window = Tk()
window.title('Рандомайзер.org')
window.geometry('300x300')
window.resizable(False, False)

label = Label(window, text='Рандомайзер')
result = Label(window, text='', font='arial 20')
label_b = Label(window, text='От')
label_a = Label(window, text='До')
entry_before = Entry(window)
entry_after = Entry(window)
btn = Button(window, text='Получить число', command=random_number)

label.place(x=110, y=20)
label_b.place(x=70, y=80)
label_a.place(x=70, y=110)
entry_before.place(x=90, y=80)
entry_after.place(x=90, y=110)
btn.place(x=100, y=140)
result.place(x=149, y=220)






mainloop()