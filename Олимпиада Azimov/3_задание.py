def decoding(word):
    if len(word) == 6:
        decoding_word = word[0] + word[2] + word[4] + word[5] + word[3] + word[1]
        print(decoding_word)
    else:
        print('Длина слова не подходит для расшифровки')
decoding('avzoim')