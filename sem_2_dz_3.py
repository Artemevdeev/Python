# Задайте список из n чисел последовательности $(1+1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
 
n = int(input('Введите число  = '))
sum = 0
x = 0
my_list = []
print('{', end = ' ')
for i in range(1,n + 1):
    x = round((1+1/i)**i,2)
    print( i,':', x,',',end = ' ')
    my_list.append(x)
    sum = sum + x
  
print ('}')
print('Cумма чисел последовательности = ',sum)
print(my_list)


