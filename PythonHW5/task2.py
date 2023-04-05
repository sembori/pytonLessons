# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
# 2 2
#     4

numA = int(input('Сейчас мы сложим два числа чрезвычайно странным способом. Итак, введите первое число:'))
numB = int(input('Введите второе число:'))


def rekursiveSum(a, b):


    if a == 0:
        return b
    return rekursiveSum(a - 1, b + 1)


print(f'Сумма = {rekursiveSum(numA, numB)}')