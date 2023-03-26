from tkinter import *
import webbrowser
def open_browser():
    path = entry.get()
    webbrowser.open(path, new=2)

window = Tk()
window.geometry(f'300x300+{window.winfo_screenwidth() // 2 - 150}+{window.winfo_screenheight() // 2 - 150}')
window.title('Hacker_Programm')
window.configure(background='black')
for r in range(3):
    window.rowconfigure(index=r, weight=1)
for c in range(2):
    window.columnconfigure(index=c, weight=1)

label = Label(window, text='Введи адрес сайта ниже',
              font='arial 15', background='black', foreground='white')
entry = Entry(window, background='black', foreground='white', font='arial 18')
btn = Button(window, text='Готово', background='black',
             foreground='red', font='arial 15', width=5, command=open_browser)

label.grid(row=0, column=0, sticky=NSEW, columnspan=2)
entry.grid(row=1, column=0, sticky=EW, columnspan=2)
btn.grid(row=2, column=0, sticky=NSEW, columnspan=2)




mainloop()