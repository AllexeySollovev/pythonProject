# from tkinter import *
#
# def on_click():
#     if r_var.get() == 0:
#         label['bg'] = 'red'
#     elif r_var.get() == 1:
#         label['bg'] = 'green'
#     elif r_var.get() == 2:
#         label['bg'] = 'blue'
#
#
#
#
#
# window = Tk()
# # r_var = BooleanVar()
# r_var = IntVar()
# r_var.set(0)
#
# red = Radiobutton(text='Red', variable=r_var, value=0, command=on_click)
# green = Radiobutton(text='Green', variable=r_var, value=1, command=on_click)
# blue = Radiobutton(text='Blue', variable=r_var, value=2, command=on_click)
#
# label = Label(width=20, height=10)
#
# red.pack()
# green.pack()
# blue.pack()
# label.pack()
# window.mainloop()


from tkinter import *
from Randxyz import choice
from tkinter.messagebox import * #импорт окна информации из готовых окон messagebox

# def on_click():
#     showinfo(title='Error 404', message='Привет')

window = Tk()
window.geometry('700x300')
window.resizable(False, False)
window.title('Викторина')



for c in range(2):
    window.columnconfigure(index=c, weight=1)

for r in range(4):
    window.rowconfigure(index=r, weight=1)

font = 'arial 12 bold'



label = Label(text='Добро пожаловать в приложение "Викторина"\n'
                   'Для запуска нажмите кнопку "Далее"\n'
                   'Для ответа на вопрос выберите вариант ответа\n'
                   'После ответа нажмите "Далее" для перехода к новому вопросу', font=font)

label.grid(row=0, column=0, columnspan=2, sticky=NSEW)


list_of_questions = [
    ['Выберите цифру 1',['1', '2', '3', '4'], 0],
    ['Выберите цифру 6',['345', '6', '544', '33'], 1],
    ['Выберите цифру 3',['1', '2', '3', '4'], 2],
    ['Выберите цифру 4',['1', '2', '3', '4'], 3]
]

# Список под текущий вопрос
new_questions = []
# Переменная, ведущая подсчет оставщихся вопросов
count = len(list_of_questions)

def correct(ans):
    if ans.get() == new_questions[2]:
            showinfo(title='Викторина', message='Ваш ответ указан верно! Вы молодец!!!')
    else:
        showerror(title='Викторина', message='Ответ указан неверно!')

def next_questions():
    global count
    global new_questions
    answer = IntVar()
    answer.set(5)

    if count != 0:
        new_questions = list_of_questions.pop(list_of_questions.index(choice(list_of_questions)))
        label['text'] = new_questions[0]


        r = 1
        c = 0
        for i in range(len(new_questions[1])):
            Radiobutton(window, text=new_questions[1][i], font=font, variable=answer, value=i,
                        command=lambda: correct(answer)).grid(row=r, column=c, sticky=NSEW)
            c += 1
            if c == 2:
                r += 1
                c = 0
        count -= 1

    elif count == 0:
        showinfo(title='Викторина', message='Вы стали победителем шоу "Кто хочет стать милионером"\n'
                                            'Выйти вы можете нажав на кнопку "Выход"')
        b_question['state'] = DISABLED

b_quit = Button(window, text='Выход', command=window.destroy)
b_quit.grid(row=3, column=0, sticky=NSEW, pady=6, padx=6)

b_question = Button(window, text='Далее', command=next_questions)
b_question.grid(row=3, column=1, sticky=NSEW, pady=6, padx=6)









window.mainloop()