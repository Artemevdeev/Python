# Реализуйте алгоритм перемешивания списка
my_list = []
for i in range(5):
    num = int(input('Введите число  = '))
    # my_list = []
# for i in range(5):
    my_list.append(num)
print(my_list)
i=0
while(i+1 < len(my_list)):
    c = my_list[i]
    my_list[i] = my_list[i-1]
    my_list[i-1] = c
    i=i+1
print(my_list)
 
