from random import randint, choice
audit = {}
teacher = {}
time = {}
teaches = ['Hynes', 'Alvarado', 'Rich', 'Berk', 'Li']
timers = ['10:00', '9:00']
for i in range(5):
    audit[f'CS10{i}'] = randint(1000, 5000)
    teacher[f'CS10{i}'] = choice(teaches)
    time[f'CS10{i}'] = choice(timers)

print(audit)
print(teacher)
print(time)