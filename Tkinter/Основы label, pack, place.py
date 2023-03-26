# from tkinter import *
#
# def button1Click():
#     Answer.config(text='Это радует!')
#
# def button2Click():
#     Answer.config(text='Это печально)')
#
#
#
# Window = Tk()
# Display = Label(Window, text='Привет! Как дела?')
# Display.pack()
#
#
#
# Answer = Label(Window, text='')
# # Компонент Button - создает кнопку
# Button_1 = Button(Window, text='Хорошо', command=button1Click)
# Button_2 = Button(Window, text='Плохо', command=button2Click)
# Button_1.pack(side='left')
# Button_2.pack(side='right')
# Answer.pack()
#
#
# Window.mainloop()
#
#
#
#
# from tkinter import *
#
# def button1Click():
#     Display.config(text='Это радует!')
#
# def button2Click():
#     Display.config(text='Это печально)')
#
#
#
# Window = Tk()
# Window.config(width=260, height=120)
# Display = Label(Window, text='Привет! Как дела?')
# Display.place(x=50, y=20, width=160, height=40)
#
#
#
#
# # Компонент Button - создает кнопку
# Button_1 = Button(Window, text='Хорошо', command=button1Click)
# Button_2 = Button(Window, text='Плохо', command=button2Click)
# Button_1.place(x=20, y=80, width=100, height=20)
# Button_2.place(x=140, y=80, width=100, height=20)
#
#
#
# Window.mainloop()




from tkinter import *

window = Tk()
window.geometry('500x350')

window.mainloop()




















