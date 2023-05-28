num = int(input('Введите номер места '))

if num%2 == 0:
    print('Верхнее')
else:
    print('Нижнее')

if num > 36:
    print('Боковое место')
else:
    print('Место в купе')