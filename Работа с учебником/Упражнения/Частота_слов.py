with open('Частота_слов.txt', 'r', encoding='utf-8')as file:
    infile = file.read()
    filelst = infile.split(' ')
    for word in filelst:
        if word.lower().rstrip() == 'это':
            print('t')



