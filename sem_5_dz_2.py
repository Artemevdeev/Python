# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


import random

player_1 = input('Введите имя 1-го игрока = ')
player_2 = input('Введите имя 2-го игрока = ')
sum_candy = 100
max_motion = 28 
curent_player = random.choice([player_1,player_2])
while sum_candy > max_motion:
    print(f'Остаток конфет = {sum_candy}')
    while True:
        take_candys = int(input(f'Сколько берет конфет ? {curent_player}'))
        if take_candys >= 1 and take_candys <=max_motion:
            break
    sum_candy -= take_candys
    curent_player = player_2 if curent_player == player_1 else player_1
print(f'Победитель =  {curent_player}')
        
        



