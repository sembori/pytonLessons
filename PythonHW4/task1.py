# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

howElementsInSet1 = int(input('Количество элементов первого множества:'))
howElementsInSet2 = int(input('Количество элементов второго множества:'))
array1 = [random.randint(0, 99) for _ in range(howElementsInSet1)]
array2 = [random.randint(0, 99) for _ in range(howElementsInSet2)]
print(array1)
print(array2)
set1 = set.union(set(array1), set(array2))
arrayResult = []
for i in set1:
    arrayResult.append(i)
print(arrayResult)
def sort(array):
    if len(array) < 1:
        return array

    else:
        centre = array[0]
    littles = [i for i in array[1:] if i <= centre]
    bigger = [j for j in array[1:] if j > centre]
    return (sort(littles) + [centre] + sort(bigger))


print(sort(arrayResult))
