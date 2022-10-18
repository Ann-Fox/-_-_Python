#  Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import os

def clear(): return os.system('cls')

clear()
print('Игра в конфеты (условие) \n')
print('На столе лежит 2021 конфета.\n Играют два игрока делая ход друг после друга. \n Первый ход определяется жеребьёвкой. \n За один ход можно забрать не более чем 28 конфет.\n Все конфеты оппонента достаются сделавшему последний ход.\n Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?')
start = input('Нажмите Enter для продолжения \n')
# Цикл ввода имени первого игрока
clear()
candy = input('Введите количество конфет: ')
if not candy:
    candy = 2021
else:
    candy = int(candy)
print(candy)
flags = True
while flags:
    player1 = input('Введите имя первого игрока: ')
    clear()
    if not player1:
        print("Имя игрока не введено, необходимо ввести имя игрока: ")
    else:
        flags = False
# Цикл ввода имени второго игрока
flags = True
while flags:
    player2 = input('Введите имя второго игрока: ')
    clear()
    if not player2:
        print("Имя игрока не введено, необходимо ввести имя игрока")
    else:
        flags = False
clear()
# Введены имена игроков
flags_winner = True
flags=True
move=0
quantity_candy_player1=0
quantity_candy_player2=0
while candy>0:
    clear()
    move +=1
    flags=True
    while flags:
        part=1
        print(f'Раунд {move} / {part} \n Конфет у игрока {player1} - {quantity_candy_player1}\n Конфет у игрока {player2} - {quantity_candy_player2} \n Осталось конфет {candy}')
        try:
            player1_candy = int(input(f'{player1} введите количество конфет,которые хотите взять от 1 до 28 - '))
            clear()
            if 1 <= player1_candy <= 28 and player1_candy <= candy:
                candy -= player1_candy
                quantity_candy_player1+= player1_candy
                flags = False
            else:
                print("Введено некорректное количество конфет")
        except ValueError:
                print('Введено некорректное количество конфет')
    flags = True
    if candy==0:
        flags=False
    while flags:
        part=2
        print(f'Раунд {move} / {part} \n Конфет у игрока {player1} - {quantity_candy_player1}\n Конфет у игрока {player2} - {quantity_candy_player2} \n Осталось конфет {candy}')
        try:
            player2_candy = int(input(f'{player2} введите количество конфет,которые хотите взять от 1 до 28 - '))
            clear()
            if 1 <= player2_candy <= 28 and player2_candy <= candy:
                candy -= player2_candy
                quantity_candy_player2+= player2_candy
                flags = False
            else:
                print("Введено некорректное количество конфет")
        except ValueError:
                print('Введено некорректное количество конфет')
        if candy ==0:
            flags_winner=False
clear()
if flags_winner==True:
    print(f'Выиграл игрок {player1}\n  у него {player1_candy} конфет')
else:
    print(f'Выиграл игрок {player2}\n  у него {player2_candy} конфет')
print(f"Количество раундов {move}")

