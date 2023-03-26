# myset = set('абв')
# print(myset)

# myset = set('аaббв')
# print(myset)

# myset = set('один', 'два', 'три')
# print(myset)

# myset = set(['один', 'два', 'три'])
# print(len(myset))


# Добавление и удаление элементов
# myset = set()
# myset.add(1)
# myset.add('Hello')
# myset.add(2)
# print(myset)

# myset = set([1,2,3])
# myset.update(['a', 'b', '6'])
# myset.update([4,5,6])
# print(myset)

# myset = set([1,2,3,4,5])
# print(myset)
# myset.remove(1)
# print(myset)
# myset.discard(6)
# print(myset)


# myset = set([1,2,3,4,5])
# myset.clear()
# print(myset)

# Объединение множеств
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print(a | b)
# a = a.union(b)
# print(a)
# b = b.union(a)
# print(b)

# Пересечения множеств
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print(a & b)
# a = a.intersection(b)
# print(a)
# b = b.intersection(a)
# print(b)


# Определение разницы множеств
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print(a - b)
# print(b - a)
# print(a.difference(b))


# Симметричная разница множеств
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print(a ^ b)
# print(a.symmetric_difference(b))




# Перебор элементво множества
# my = {'Go', 'Python', 'C++'}
# for i in my:
#     print(i)
#
#
# my_skills = {'python', 'flask', 'django', 'критическое мышление',
#              'переговоры', 'планирование', 'html'}
# backend = {'python', 'terminal', 'django', 'linux'}
# frontend = {'html', 'css', 'javascript'}
# soft_skills = {'критическое мышление', 'переговоры',
#                'планирование', 'лидерство'}
#
# # Каких frontend навыков не хватает программисту
# frontend_i = frontend.difference(my_skills)
# # Какие backend навыки есть у программиста
# backend_i = my_skills.intersection(backend)
# # Не frontend  не backend навыки
# non_skills = my_skills.difference(backend).difference(frontend_i)
# print(non_skills)
#
#
# baseball = set(['Джоди', 'Кармен', 'Аида', 'Алиция'])
# basketball = set(['Эва', 'Кармен', 'Алиция', 'Сара' ])
# print(f'Эти студенты состоят в бейсбольной команде: {baseball}')
# print(f'Эти студенты состоят в баскетбольной команде: {basketball}')
# print(f'Эти студенты состоят в баскетбольной и бейсбольной команде: {basketball.intersection(baseball)}')
# print(f'Эти студенты играют в одну или обе спортивные игры: {basketball.union(baseball)}')
# print(f'Эти студенты состоят в баскетбольной, но не состоят в бейсбольной команде: {basketball.difference(baseball)}')
# print(f'Эти студенты состоят в бейсбольной, но не состоят в баскетбольной команде: {baseball.difference(basketball)}')
#
#





with open('gfg.txt', 'r')as file:
    for line in file:
        print()






