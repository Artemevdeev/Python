# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

num = int(input('Введите число = '))

def Fb(num):
    if num == 1 or num == -1:
        return 1
    elif num == 0:
        return 0
    else:
        if num > 0:
            return Fb(num - 1)+Fb(num - 2)    
        elif num < 0:
            return Fb(num + 2)-Fb(num + 1)

for i in range(-num,num+1):
    print(Fb(i), end = ' ')



