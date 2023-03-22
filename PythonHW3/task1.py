'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
'''

import random

listLen = int(input('Сколько элементов будет в списке:'))
myList = [random.randint(1, 10) for i in range(listLen)]
number = int(input('Какое число проверить:'))
count = 0
for i in range (0,len(myList)):
    if myList[i] == number:
        count += 1
print(myList)
print(count)
