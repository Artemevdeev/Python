# r - чтение
# w - запись
# a - дозапись


# file_path = r'file.txt'
# f = open(file_path, 'w')
# f.write('123')
# f.close()




# 1. Задайте строку из набора чисел.
#  Напишите программу, которая покажет большее и меньшее число.
#  В качестве символа-разделителя используйте пробел.


file_path = r'file.txt'
with open(file_path,'r') as f:
        mystr = f.read()
print(mystr)
mystr = mystr.split()

print(mystr)
for i in range(len(mystr)):
    mystr[i] = int(mystr[i])
print(mystr)
print(max(mystr))
print(min(mystr))






# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python
    

# 2. Найдите корни квадратного уравнения
# Ax² + Bx + C = 0
# двумя способами:
#
# 1) с помощью математических формул нахождения корней квадратного уравнения


# path = 'file.txt'
# with open(path, 'r') as my_file:
#     data = my_file.read()

# data = data.split()
# print(data)
# data = data[:-2]
# print(data)
# data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
# print(data)
# # D=b^2-4ac
# d = data[1]**2 - 4 * data[0] * data[2]
# print(d)
# # x=((-b+(d^(1/2)))/(2*a))
# x_1 = (-data[1] + d**0.5) / (2 * data[0])
# x_2 = (-data[1] - d**0.5) / (2 * data[0])
# print(x_1, x_2)



# data = open('ert.txt', 'w')

# data.writelines('\nLesson 5')

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))

# d = b**2-4*c*a
# x1 = (-b+d**0.5)/(2*a)
# x2 = (-b-d**0.5)/(2*a)

# data.writelines(f'\n {a}*x^2+{b}*x+{c}=0 \nx1 = {x1},    \nx2 = {x2}')
# data.close









# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
