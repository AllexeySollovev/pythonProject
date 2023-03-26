def convert_number_to_word(num):
    count = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    count_eleven_to_nineteen = ['одиннадцать',
                                'двенадцать',
                                'тринадцать',
                                'четырнадцать',
                                'пятнадцать',
                                'шестнадцать',
                                'семнадцать',
                                'восемнадцать',
                                'девятнадцать']
    count_decimal = ['десять',
                     'двадцать',
                     'тридцать',
                     'сорок',
                     'пятьдесят',
                     'шестьдесят',
                     'семьдесят',
                     'восемьдесят',
                     'девяносто']
    if num > 10 and num <= 19:
        print(count_eleven_to_nineteen[num - 11])
    elif len(str(num)) == 1:
        print(count[num-1])
    else:
        print(count_decimal[num // 10 - 1] + ' ' + count[num % 10 - 1])

convert_number_to_word(78)
convert_number_to_word(12)
