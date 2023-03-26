from tkinter import *
from tkinter import filedialog
import webbrowser
import sys

window = Tk()
window.title('Блокнот 2.0')
window.geometry(f'700x300+{window.winfo_screenwidth() // 2 - 350}+{window.winfo_screenheight() // 2 - 150}')
def open_site():
    webbrowser.open("www.youtube.com/watch?v=pXnpsBBBMo4", new=0, autoraise=True)

def save_file():
    path = filedialog.asksaveasfilename(defaultextension='txt',
                                        filetypes=
                                        (('Текст', '*.txt'),
                                        ('Python', '*.py'))) #создаем путь для файла и задаем критерии сохранения
    if path != '':
        lst = text.get(1.0, END).split('\n')
        with open(path, 'w', encoding='utf-8')as file:
            for line in lst:
                file.write(line + '\n')

def open_file():
    path = filedialog.askopenfilename()
    if path != '':
        with open(path, 'r', encoding='utf-8')as file:
            lst = file.readlines()
            text.insert(1.0, ''.join(lst))

def open_author():
    authors = Toplevel()
    label = Label(authors, text='Программа <Блокнот 2.0>\n'
                                'Создана автором - <Алексей Соловьёв>\n'
                                'Разработка произведена в рамках курса <Программирование на Python>')
    label.pack()

def change_background():
    text['bg'] = 'white'
def change_background_to_red():
    text['bg'] = 'red'

def open_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

for r in range(8):
    window.rowconfigure(index=r, weight=1)
for c in range(12):
    window.columnconfigure(index=c, weight=1)

text = Text(window,
            width=25, height=5,
            background='white', foreground='black',
            wrap=WORD, font='arial 15')
text.grid(row=0, column=0, sticky=NSEW, rowspan=8, columnspan=12)

scroll = Scrollbar(command=text.yview)
scroll.grid(row=0, column=12, sticky=NSEW, rowspan=8)
text.config(yscrollcommand=scroll.set)

main_menu = Menu(window)
window.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить как', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=window.destroy)
main_menu.add_cascade(label='Файл', menu=file_menu)

about_menu = Menu(main_menu, tearoff=0)
about_menu.add_command(label='О программе', command=open_site)
about_menu.add_command(label='Автор', command=open_author)
main_menu.add_cascade(label='Справка', menu=about_menu)

context_menu = Menu(window, tearoff=0)
context_menu.add_command(command=change_background, label='Изменить фон на "white"')
context_menu.add_command(command=change_background_to_red, label='Изменить фон на "red"')
window.bind('<Button-3>', open_context_menu)

mainloop()


