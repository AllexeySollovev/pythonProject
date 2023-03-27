from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path
from tkinter import *
from tkinter.filedialog import *

def pdf_to_mp3(file_path='test.pdf', language='en'):
    process_info = Text(window, height=10)
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        for widget1 in widgets1:
            widget1.destroy()

        process_info.pack(side='top')
        btn_next = Button(window, text='Продолжить конвертировать', width=10)
        process_info.insert(1.0, f'[+] Original FileName : {Path(file_path).name}\n')
        process_info.insert(END, '[+] Processing...\n')


        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        process_info.insert(END, f'[+] {file_name}.mp3 saved succesfully!\n----Have a good day!----')
        return ''
    else:
        process_info.insert(END, 'File not exists, check the file path!')
        return ''

def convert_to_mp3():
    file_name = askopenfile()
    if file_name:
        file_name = file_name.name
    print(pdf_to_mp3(file_path=file_name, language=language1))


window = Tk()
label = Label(window, text='PDF>>TO>>MP3', font='bulbhead')
label.pack(side='top')
radio = IntVar()
radio.set(0)
labellang = Label(window, text='Choose Language')
labellang.pack(side='top', padx=10, pady=10)
languages = Frame(window)
languages.pack(side='top')
english = Radiobutton(languages, text='en', width=10, variable=radio, value=1)
russian = Radiobutton(languages, text='ru', width=10, variable=radio, value=2)
english.pack(side='left')
russian.pack(side='right')
language1 = 'en' if radio.get() == 1 else 'ru'
button_path = Button(window, text='Перевести в mp3', width=50, command=convert_to_mp3)
button_path.pack(side='top')
widgets1 = [label, labellang, languages, button_path]
mainloop()

