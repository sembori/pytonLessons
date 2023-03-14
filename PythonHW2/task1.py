'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
'''
from random import randint
coins = randint(5, 30)
count = 0
cointStatus = 0
heads = 0
tails = 0

while count<=coins:
    cointStatus = randint(0,1)
    if cointStatus == 1:
        heads += 1
    else:
        tails+=1
    count+=1
    print(cointStatus, end =' ')
if heads < tails:
    print(f'\n Минимум необходимо перевернуть {heads} монет')
else:
    print(f'\n Минимум необходимо перевернуть {tails} монет')

