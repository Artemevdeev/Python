# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0\
import random


k = 2
my_list = []
for i in range(k,0,-1):
    my_list.append(f'{random.randint(0,100)}*x^{i}')
print(my_list)

result = ' + '.join(my_list) + f' + {random.randint(0,100)} = 0'
print(result)

with open ('text.txt','w') as file:
    file.write(result)


