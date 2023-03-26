import turtle

t = turtle.Turtle()
#
# t.speed(100)
# turtle.bgcolor('black')
#
# for i in range(240):
#     t.color('cyan')
#     t.circle(i)
#     t.left(5)
#
# turtle.done()

#Поворот черепахи направо
# t.forward(200)
# t.right(90)
# t.forward(200)

#.heading() - Указывает текущее направление черепахи
#.setheading() - установка угла черепахи в заданный угол
# t.forward(50)
# t.setheading(90)
# t.forward(100)
# t.setheading(180)
# t.forward(50)
# t.setheading(270)
# t.forward(100)


#turtle.penup() - Поднятие пера
#turtle.pendown() - Опускание пера

# t.forward(50)
# t.penup()
# t.forward(25)
# t.pendown()
# t.forward(50)
# t.penup()
# t.forward(25)
# t.pendown()
# t.forward(50)

#.circle(радиус) - Начертит круг с заданным радиусом

# t.circle(100)


#.dot() - Указывает черепахе начертить точку

# t.dot()
# t.forward(50)
# t.dot()
# t.forward(50)
# t.dot()
# t.forward(50)

#.pensize(ширина) - Изменение ширины пера

# t.pensize(5)
# t.circle(100)


#.pencolor(цвет, или ничего - покажет используемый цвет) - Изменение цвета пера
#.bgcolor(цвет) - Меняет цвет фона

# turtle.bgcolor('gray')
# t.pencolor('red')
# t.circle(100)


#.setup(ширина,высота) - Установление размера окна

# turtle.setup(1280,960)


#.goto(x,y) - Перемещение черепахи в конкретную позицию
#.pos() - Текущая позиция черепахи
#.xcor() - Отображение текущей позиции х
#.ycor() - Отображение текущей позиции y

# t.goto(100, 150)
# t.xcor()

#.speed(0, 1-10) - 0 это отключение анимации, 1-10 скорость

# t.speed(0)
# t.circle(100)

#.hideturtle() - Скрыть черепаху
#.showturtle() - Показать черепаху

#.write(текст) - Вывод текста в графическое окно

# t.write('Привет, мир!')

#Перемещение текста по графическому окну

# turtle.setup(500,500)
# t.penup()
# t.hideturtle()
# t.goto(150,230)
# t.write('Справа вверху')
# t.goto(-230,-230)
# t.write('Слева внизу')



#.begin_fill() - Запуск черчения фигуры
#.end_fill() - Прекращение черчения фигуры
#.fillcolor(цвет, или ничего - вернет используемый цвет) - Цвет фигуры

# t.hideturtle()
# t.fillcolor('blue')
# t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.end_fill()


#.numinput(заголовок, подсказка, default=x, minval=y, maxval=z) - Создать диалоговое окно
#default=x - Это значение по умолчанию, оно изначально вводится в панель ввода
#minval=y - Это минимально допустимое значение ввода
#maxval=z - Это максимально допустимое значение ввода
#
# interview = turtle.numinput('Ты лох?', '1 - ДА или  0 - НЕТ')
# if interview == 1:
#     turtle.numinput('', 'хаха ты лох!!!')
# if interview == 0:
#     turtle.numinput(' ', 'Тогда ты чмо')

# radius = turtle.numinput('Требуются данные', 'Введи радиус окружности', default=100)
# t.circle(radius)


#.textinput() - Тоже самое что и .numinput(), но используется для ввода строковых данных

# name = turtle.textinput('Требуются данные', 'Введите свое ФИО')
# print(name)
#ПРАКТИКА
# t.hideturtle()
# t.fillcolor('blue')
# t.begin_fill()
# t.forward(300)
# t.left(90)
# t.forward(300)
# t.left(90)
# t.forward(300)
# t.left(90)
# t.forward(300)
# t.end_fill()


# radius = turtle.numinput('Введите значение', 'Каков радиус окружности?')
# t.circle(radius)


# .isdown() - Возвращает истину если перо черепахи опущено, ложь если поднято
# .isvisible() - Возвращает истину если черепаха видима, ложь если невидима
# .heading() - ВЫВОДИТ ТЕКУЩЕЕ УГЛОВОЕ направление черепахи
#   ЕСЛИ ВВОДИТ ФУНКЦИИ БЕЗ ВВОДА ЗНАЧЕНИЯ - ВЫВОДИТСЯ ЗНАЧЕНИЕ КОТОРОЕ ИСПОЛЬЗУЕТСЯ

# t.speed(0)
# t.hideturtle()
# radius = 20
# for count in range(20):
#     t.circle(radius)
#     x = t.xcor()
#     y = t.ycor() - 10
#     radius = radius + 10
#     t.penup()
#     t.goto(x, y)
#     t.pendown()

# t.speed(0)
# t.hideturtle()
# t.penup()
# t.goto(-200, 0)
# t.pendown()
# for x in range(36):
#     t.forward(400)
#     t.left(170)


# f = 10
#
# t.speed(0)
# t.hideturtle()
# for x in range(52):
#     t.forward(f)
#     t.left(90)
#     f = f + 10

t.speed(9)


t.circle(90)
t.penup()
t.forward(180)
t.pendown()
t.circle(90)
t.left(180)
t.penup()
t.forward(115)
t.right(90)
t.forward(140)
t.pendown()
t.forward(100)






turtle.done()

