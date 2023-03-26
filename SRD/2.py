# count = 0
# num = -1
# while num != 0:
#     num = int(input('Введите число. 0 - Выход'))
#     if num % 3 == 0 and num % 12 != 0:
#         count += 1
#print(count)

from random import randint
# num = -1
# while num != 0:
#     num = randint(0,100)
#     print(num)

#
# min = 0
# max = 0
# num = -1
# while num % 5 != 0:
#     num = randint(0, 100)
#     if num > max:
#         max = num
#     if num < min:
#         min = num
# print(f'Макс число {max}')
# print(f'Мин число {min}')


#
# chet = 0
# nechet = 0
# num = -1
# while num != 0:
#     num = int(input('Введите число, 0 - выход: '))
#     if num == 0:
#         break
#     even = 0
#     add = 0
#     while num > 0:
#         if (num % 10) % 2 == 0:
#             even += 1
#         else:
#             add += 1
#         num //= 10
#     num = -1
#     print(f'Четных: {even}, Нечетных: {add}')


# num = -1
# while num != 0:
#     num = int(input('Введите число, 0 - выход: '))
#     print(num * (num - 1))

#
# num = 0
# while num != 778:
#     print(num)
#     num += 1



num = -1
while num % 25 != 0:
    num = randint(0, 1000)
    print(f'число {num}')
    print(num % 10 * num // 10 * num // 100 * num // 1000)




