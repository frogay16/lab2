color1 = input('Введите первый цвет ')
color2 = input('Введите второй цвет ')

if color1 == 'красный' and color2 == 'синий' or color2 == 'красный' and color1 == 'синий':
    print('фиолетовый')
elif color1 == 'красный' and color2 == 'желтый' or color2 == 'красный' and color1 == 'желтый':
    print('оранжевый')
elif color1 == 'желтый' and color2 == 'синий' or color2 == 'желтый' and color1 == 'синий':
    print('зеленый')
elif color1 == color2:
    print(color1)
else:
    print('Ошибка')