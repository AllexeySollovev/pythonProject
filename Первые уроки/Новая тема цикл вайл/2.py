#Логическая переменная
#bolean =True
#while(bolean):
#    y = input('Введите слово:')
#   if (y == '1'):
#       print('Ты дал верный ответ')
#        bolean = False
#    else:
#        print("моя не понимать тебя")
playgame = True
while(playgame):
    w =input("Введите кодовое слово 'End': ")
    if(5==5):
        print("Я выполнюсь")
    if(w =="End"):
        print("Ты активировал Ядерный Реактор")
        playraund = True
        if(playraund):
            print("До взрыва осталось 60 секунд")
            while True:
                print("Какой провод хочешь перекусить?")
                q=input("Красный или Синий?")
                if(q == "Красный"):
                    print("Ты перекусил ошибочный вариант, Мир Уничтожен!")
                    break
                elif(q == "Синий"):
                    print("Молодец! Ты спас Мир!")
                    break
