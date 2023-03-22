'''Требуется найти в массиве A[1..N] самый близкий по величине элемент к
 заданному числу X. Пользователь в первой строке вводит натуральное число
 N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
 Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
'''
import random
listLen = int(input('Сколько элементов будет в списке:'))
myList = [random.randint(1, 21) for i in range(listLen)]
number = int(input('Какое число проверить:'))
print(myList)
bigger = 21
little = 0
for i in range(0, listLen):
    if number > myList[i] > little:
        little = myList[i]
    elif bigger > myList[i] > number:
        bigger = myList[i]
print(f'Близжайшее меньшее число: {little}')
print(f'Близжайшее большее число: {bigger}')
