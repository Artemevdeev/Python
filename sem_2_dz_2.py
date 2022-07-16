#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# num = int(input('Введите число  = '))
# result = 1
# for i in range(1,num+1):
#     result = i * result
#     print(result, end =' ')

num = int(input('Введите число  = '))
my_list = []
result = 1
for i in range(1,num+1):
    result = i * result
    my_list.append(result)
print(my_list)
