# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число = '))
my_list =[]
while num > 1:
    num1 = num % 2
    num = num // 2
    my_list.append(num1)
my_list.append(num)
print(my_list)
for i in range(len(my_list)):
    print(my_list[-(i + 1)], end = '')

# def transform(num):
#     new_string = ''
#     result = ''
#     print(f'Число {num} в двоичной системе:', end=' ')
#     while num > 1:
#         new_string += str(num % 2)
#         num //= 2
#     new_string += str(num)
#     for i in range(len(new_string)):
#         result += new_string[-(i+1)]
#     return result

# transform(2)