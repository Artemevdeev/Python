# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти = '))
if (num == 1):
    print('х > 0 and y > 0')
if (num == 2):
    print('х < 0 and y > 0')
if (num == 3):
    print('х < 0 and y < 0')
if (num == 4):
    print('х > 0 and y < 0')
if (num < 1 or num > 4):
    print('Вы ввели некорректный номер четверти')
