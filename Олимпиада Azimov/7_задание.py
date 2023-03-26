with open('lunch.txt', 'r', encoding='utf-8')as file:
    for line in file:
        count = line.split()
M = int(count[0])
K = int(count[1])
N = int(count[2])
print(f'{int(N / K)} - максимальное количество деталей,'
      f' которое сможет сделать сотрудник за время равное - {N} миллисекунд')
