# Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите натуральное число - '))
def prime_number(num):
    for i in range(2, int(num**0.5 + 1 )):
        if num % i == 0:
            return False 
    return True 
my_list = []
for i in range(2,num):
    if num % i == 0 and prime_number(i):
        my_list.append(i)
print(my_list)



