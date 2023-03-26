from random import randint

count = 0
result = ''
while 'PPPP' not in result and 'OOOO' not in result:
    coin = randint(0, 1)
    if coin == 0:
        result = result + 'O'
        count += 1
    elif coin == 1:
        result = result + 'P'
        count += 1
print(f'{result} ({count} попыток)')






