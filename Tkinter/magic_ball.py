# from tkinter import *
#
# def on_click():
#     text['text'] = text_enter.get()
#     text_enter.delete(0, END)
#
#
# window = Tk()
# window.geometry('300x200')
# window.resizable(False, False)
#
# text = Label(window, text='текст')
# text.place(anchor=CENTER, x=145, y=20)
#
#
# text_enter = Entry(window, background='gold', foreground='red', font='arial 12',
#                    justify=LEFT, show='', cursor='watch')
#
#
# text_enter.place(anchor=CENTER, x=145, y=50)
#
# # insert() - Вставка строки string на место index
# text_enter.insert(0, 'Введите текст')
#
# btn = Button(window, text='Ввод', command=on_click)
# btn.place(anchor=CENTER, x=145, y=90)
#
#
#
#
#
#
#
#
#
#
#
# window.mainloop()


from tkinter import *
import time
from Randxyz import choice

answers = ['Бесспорно', 'Так точно', 'Определенно да', 'Конечно',
           'Мне кажется, да', 'Вероятнее всего', 'Можеть быть', 'Скорее да',
           'Пока не ясно', 'Наверно', 'Спроси позже', 'Я не уверен',
           'Нет', 'Весьма сомнительно', 'Определенно нет', 'Звезды говорят - "нет"']
count_bad = 0

def answer():
    global count_bad
    question = question_enter.get()
    if question == '' or question[0] in '1234567890-=+*@%':
        count_bad += 1
        if count_bad == 1:
                window.config(background='#ffd6d6')
                text1.config(background='#ffd6d6')
                text2.config(background='#ffd6d6')
                text3.config(background='#ffd6d6')
                btn.config(background='#ffd6d6')
                text3['text'] = 'Вы ввели неккоректные данные'


        elif count_bad == 2:
            window.config(background='#ff6767')
            text1.config(background='#ff6767')
            text2.config(background='#ff6767')
            text3.config(background='#ff6767')
            btn.config(background='#ff6767')
            text3['text'] = 'Проверь правильность регистра!!!'

        else:
            window.config(background='#ff1f1f')
            text1.config(background='#ff1f1f')
            text2.config(background='#ff1f1f')
            text3.config(background='#ff1f1f')
            btn.config(background='#ff1f1f')
            text3['text'] = '\nПОСЛЕДНЕЕ ПРЕДУПРЕЖДЕНИЕ\n ПРЕКРАТИ СЕЙЧАС ЖЕ'
    else:
        window.config(background='#90ee90')
        text1.config(background='#90ee90')
        text2.config(background='#90ee90')
        text3.config(background='#90ee90')
        btn.config(background='#90ee90')
        time.sleep(2)
        text3['text'] = choice(answers)
    question_enter.delete(0, END)









window = Tk()
window.geometry('500x350')
window.resizable(False, False)
window.title('Шар-Предсказатель')

text1 = Label(window, text='Шар-предсказатель', font='arial 20')
text1.pack()
text2 = Label(window, text='Напишите чего желаете', font='arial 15')
text2.place(anchor=CENTER, x=250, y=60)


question_enter = Entry(window, width=45)
question_enter.place(anchor=CENTER, x=250, y=90)

btn = Button(window, text='Узнай свою судьбу!', font='arial 15', command=answer)
btn.place(anchor=CENTER, x=245, y=140, width=200, height=55)


text3 = Label(window, text='', font='arial 15')
text3.place(anchor=CENTER, x=250, y=190)
window.mainloop()



























