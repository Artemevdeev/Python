
# Задача. удалить из исходной строки слова с "абв"
# 'Привет, мир! Мы очеабвнь любим Пайтомаабвба! Семинары'

# str_list = 'Привет, мир! Мы очеабвнь любим Пайтомаабвба! Семинары'
# str = str.split()
# print(str)

# str_list = str_list.split()
# def strs(str):
#     for item in str_list:
#         if 'абв' in item:
#             str_list.remove(item)
#     print(str_list)
# strs(str_list)

# res = list(filter(lambda item: 'абв' not in item, str_list.split()))
# print(res)


# 1. Удалить из исходной строки все слова с "абв"
# my_str = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# res = [word for word in my_str.split() if 'абв' not in word]
# print(' '.join(res))



# Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = [ 1, 2, 3, 5, 1, 5, 3, 10]
my_list1 = []
for i in my_list:
    if my_list.count(i) == 1:
        my_list1.append(i)
print(my_list1)


my_list = [1, 2, 3, 5, 1, 5, 3, 10]
res = []
for item in my_list:
    if my_list.count(item) == 1:
        res.append(item)
print(res)


res = [item for item in my_list if (my_list.count(item) == 1)]
print(res)

f = lambda item: my_list.count(item) == 1
res = list(filter(f, my_list))
print(res)
