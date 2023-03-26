from tkinter import *

class AutoSHOP:
    def __init__(self):
        self.window = Tk()
        self.window.title('Автосервис')

        self.listbox = Listbox(self.window, width=0, height=0)
        self.listbox.pack(padx=15)
        self.listbox.bind('<<ListboxSelect>>', self.info_service)

        self.frame = Frame(self.window)
        self.frame.pack()

        self.label_count = Label(self.frame, text='Стоимость:')
        self.labvar = StringVar()
        self.labelvar_count = Label(self.frame, textvariable=self.labvar)

        self.label_count.pack(side='left')
        self.labelvar_count.pack(side='right')

        self.btnexit = Button(self.window, text='Выйти', command=self.window.destroy)
        self.btnexit.pack()
        services = ['замена масла', 'смазочные работы', 'промывка радиатора', 'замена жидкости трансмиссии',
                    'осмотр', 'замена глушителя выхлопа', 'перестановка шин']
        for service in services:
            self.listbox.insert(END, service)
        mainloop()

    def info_service(self, event):
        servicecur = self.listbox.curselection()
        service = self.listbox.get(servicecur[0])

        if service == 'замена масла':
            self.labvar.set('500р')
        elif service == 'смазочные работы':
            self.labvar.set('300р')
        elif service == 'промывка радиатора':
            self.labvar.set('700р')
        elif service == 'замена жидкости трансмиссии':
            self.labvar.set('1000р')
        elif service == 'осмотр':
            self.labvar.set('800р')
        elif service == 'замена глушителя выхлопа':
            self.labvar.set('1300р')
        elif service == 'перестановка шин':
            self.labvar.set('1300р')



if __name__ == '__main__':
    auto = AutoSHOP()