chislo=int(input("Введи трехзначное число"))
hundr=chislo//100 #Сотые
desyat=(chislo//10)%10 #десятки
ed=chislo%10  #единицы
sum=(ed*100)+(desyat*10)+hundr
print(sum)

