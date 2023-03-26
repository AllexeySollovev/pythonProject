from ctypes import*
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))


#Установка цвета для текста
def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h,c)

# Вывод текста на экран
def colorLine(c, s):
    color(c)
    print('*' * 43)
    print(f'{s}')
    print('*' * 43)

colorLine(14, '''-Дарова, ты попал в самое опасное казино,
-Будь готов ко всем испытаниям,
-Выбирай одну из трёх игр''')

#Функция для выбора пунктов из меню
def getInput(digit,message):
    color(2)
    ret = ''
    while (ret == '' or not ret in digit):
        ret = input(message)
    return ret
print(f"Вы ввели число: {getInput('0,1,2,3','Выберите пункт меню: 0,1,2,3: ')}")

#Минимальное и Максимальное значение ставки
def getIntInput(minimum,maximum,message):
    ret = -1
    while ret < minimum or ret > maximum:
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
           print('Вы ввели буквенное выражение, заместо цифренного')
    return ret

print(getIntInput(0,1000,'Сделайте ставку от 0 до 1000 рублей: '))

#Вывод сообщения о выигрыше
def pobeda(result):
    pass

#Вывод сообщения о проигрыше
def proigr(result):
    pass
