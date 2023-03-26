# def w():
#     pass
# w()
#
# def mama(kak,time):
#     print(f'Я мою пол {kak}')
#     print(f'На все про всё у меня осталось {time} минут')
# mama('быстро',30)
#
# def summa(a,b,c,d,e):
#     print(a,b,c,d,e)
# summa(1,'h',True,[],6.5)


def attention(text,):
    for i in range(1,5):
        print('>'*i)
    print('>'*5,'ВНИМАНИЕ! Важная информация')
    for i in range(4,0,-1):
        print('>'*i)
    print(text)
    x = input('1-Да 2-Нет')

attention('Вы знаете какой сегодня день?')
attention('Вы мужчина?')
attention('Ты сегодня кушал?')
