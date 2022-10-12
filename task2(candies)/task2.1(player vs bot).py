# Та же игра, но против непобедимого бота (если он начинает первым)
# Чтобы бота можно было победить, то в код, вместо формулы вычисления количества забираемых ботом конфет, добавляем рандом от 1 до 28
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
    print("По жребию начинает Бот")

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
            print("Ход Бота:")
            print(f'На столе {candies_sum} конфет(ы)')
            amount = int(candies_sum % 29)
            print(f'Бот взял {amount} конфет(ы)')
            candies_sum -= amount            
            if candies_sum == 0:
                print("На столе больше не осталось конфет!")
                player1_win = False
            whose_move = 1            
            break


if player1_win:
    print("Победитель: Игрок 1, он забирает все конфеты! Поздравляем!")
else:
    print("Победитель: Бот, он забирает все конфеты! Поздравляем!")