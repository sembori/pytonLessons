'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
numberN = int(input('Введите число:'))
stepen=2
while stepen <= numberN:
    print(stepen)
    stepen*=2
