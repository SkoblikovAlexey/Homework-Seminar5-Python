# Создайте программу для игры с конфет(ы)ами человек против человека.

# Условие задачи: На столе лежит 2021 конфет(ы)а. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(ы).
#  Все конфет(ы)ы оппонента достаются сделавшему последний ход. Сколько конфет(ы) нужно взять первому игроку,
#  чтобы забрать все конфет(ы)ы у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random
import os


def clear():
    return os.system('cls')

candies_sum = 2021
player1_win = False
whose_move = 0
lot = random.randint(0, 1)
if lot == 0:
    whose_move = 1
    print("По жребию начинает Игрок 1")
else:
    whose_move = 2
    print("По жребию начинает Игрок 2")

while candies_sum > 0:
    while True:        
        if whose_move == 1:
            print("Ход Игрока 1:")
            print(f'На столе {candies_sum} конфет(ы)')
            try:
                amount = int(input("Игрок 1, введите количество конфет(ы), которое хотите взять от 1 до 28: "))
                if 0 < amount < 29 and amount <= candies_sum:
                    candies_sum -= amount
                    print(f'На столе {candies_sum} конфет(ы)')
                    if candies_sum == 0:
                        print("На столе больше не осталось конфет!")
                        player1_win = True
                    whose_move = 2
                    clear()
                    break                    
                else:
                    print("Игрок 1, введите корректное количество конфет(ы)")
            except ValueError:
                print("Игрок 1, введите корректное количество конфет(ы)")
        else:
            print("Ход Игрока 2:")
            print(f'На столе {candies_sum} конфет(ы)')
            try:
                amount = int(input("Игрок 2, введите количество конфет(ы), которое хотите взять от 1 до 28: "))
                if 0 < amount < 29 and amount <= candies_sum:
                    candies_sum -= amount
                    print(f'На столе {candies_sum} конфет(ы)')
                    if candies_sum == 0:
                        print("На столе больше не осталось конфет!")
                        player1_win = False
                    whose_move = 1
                    clear()
                    break
                else:
                    print("Игрок 2, введите корректное количество конфет(ы)")
            except ValueError:
                print("Игрок 2, введите корректное количество конфет(ы)")

if player1_win:
    print("Победитель: Игрок 1, он забирает все конфеты! Поздравляем!")
else:
    print("Победитель: Игрок 2, он забирает все конфеты! Поздравляем!")


