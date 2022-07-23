# Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = [ 1,1,3,4,4,5,6,6]
my_list1 = []
for i in my_list:
    if my_list.count(i) == 1:
        my_list1.append(i)
print(my_list1)





# for i in range(0,len(my_list))-1:
#     for j in range (1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             continue
#         else: my_list1.append(my_list[i])
# print(my_list1)