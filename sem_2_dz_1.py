#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Введите вещественное число = ')
sum = 0
for i in num:
    if i == '.':
        continue
    sum = int(i) + sum

    
print(sum)

