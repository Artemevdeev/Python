# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3. 141.$  


num = float(input('Введите число = '))
print(num)
pi = 3.1415926535 
# num = 0.001
st1 = len(str(num)) - 2
pq = round(pi,st1)
print(pq)