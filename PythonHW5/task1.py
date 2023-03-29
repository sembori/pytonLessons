# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
numberA = int(input('Введите чесло, возводимое в сетепень:'))
grade = int(input('В какую степень его возведем:'))


def gradeRekursive(a, b):
    if b != 0:
        return a * gradeRekursive(a, b - 1)
    else:
        return 1


print(f'Число {numberA} в {grade} степени = {gradeRekursive(numberA, grade)}')
