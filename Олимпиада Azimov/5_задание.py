d = int(input('Введи число которое будет делится на 160:'))
count = 0
count_digit = 0
with open('numbers.txt', 'r', encoding='utf-8')as file:
    for line in file:
        word = int(line) % d
        if word == 160:
            count += 1
with open('numbers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if int(line) > 9 and int(line) < 100:
            count_digit += int(line)
print(count)
print(count_digit)