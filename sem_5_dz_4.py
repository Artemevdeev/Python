# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# аабббв= 2а3б1в


def  compression(my_list):
    res = ''
    count = 1
    for i in range(len(my_list)):
        if i+1 < len(my_list) and my_list[i] == my_list[i+1]:                    
            count += 1
        elif i+1 < len(my_list) and my_list[i] != my_list[i+1]:
            res += f'{count}{my_list[i]}'
            count = 1
        else:
            res += f'{count}{my_list[i]}'
            count = 1
    return res


def out(me_list):
    new_str = ''
    for i in range (len(me_list)):
        if me_list[i].isdigit() :
            num = int(me_list[i])
            while num !=0:
                new_str += f'{me_list[i+1]}'
                num = num - 1 
    return new_str



my_list = 'aaabbdbbccaa'
print(compression(my_list))
print(out(compression(my_list)))