"""tребуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
Пример:*
3 2 4 -> yes
3 2 1 -> no
"""
chocolateWidth = int(input('Сколько долек ширина шоколадки: '))
chocolateLong = int(input('Сколько долек длина шоколадки: '))
howMuchSegments = int(input('Сколько долек вы хотели бы отломить: '))
if howMuchSegments%chocolateLong == 0 or howMuchSegments%chocolateWidth == 0:
    print('Да, вы счастливчик! Столько долек отломить можно!')
else:
    print('Учитесь считать мисс или мистер. Столько долек отломить не получится')