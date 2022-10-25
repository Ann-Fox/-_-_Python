# Создайте программу для игры в ""Крестики-нолики"".
# решение: https://github.com/Alisbur

from ast import Pass
import os
import random
import time


def clear(): return os.system('cls')


clear()

# Глобальные переменные параметров игры
player1_turn = True
player1_inc = 1
player1_name = "Игрок 1"
player2_inc = -1
player2_name = "Игрок 2"

# Глобальные словари всех полей, линий и сумм линий
fields_dict = {'A1': 0, 'B1': 0, 'C1': 0, 'A2': 0,
               'B2': 0, 'C2': 0, 'A3': 0, 'B3': 0, 'C3': 0}
lines_dict = {1: ('A1', 'A2', 'A3'), 2: ('B1', 'B2', 'B3'), 3: ('C1', 'C2', 'C3'), 4: ('A1', 'B1', 'C1'), 5: (
    'A2', 'B2', 'C2'), 6: ('A3', 'B3', 'C3'), 7: ('A1', 'B2', 'C3'), 8: ('A3', 'B2', 'C1')}
lines_sums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

# Глобальные переменные макс и минимальных значений линий и их ключей в словаре
max_line_sum = 0
min_line_sum = 0
max_line_key = 1
min_line_key = 1

# Функция вывода и заполнения игрового поля и соответствия игроков и их фигур


def print_field():
    global fields_dict, player1_name, player2_name

    xo_dict = {}
    for fkey in fields_dict.keys():
        if fields_dict[fkey] == 0:
            xo_dict[fkey] = " "
        elif fields_dict[fkey] == -1:
            xo_dict[fkey] = "O"
        else:
            xo_dict[fkey] = "X"
    clear()
    print()
    print("      A     B     C ")
    print("   ┌─────┬─────┬─────┐")
    print(f" 1 │  {xo_dict['A1']}  │  {xo_dict['B1']}  │  {xo_dict['C1']}  │")
    print("   ├─────┼─────┼─────┤")
    print(f" 2 │  {xo_dict['A2']}  │  {xo_dict['B2']}  │  {xo_dict['C2']}  │")
    print("   ├─────┼─────┼─────┤")
    print(f" 3 │  {xo_dict['A3']}  │  {xo_dict['B3']}  │  {xo_dict['C3']}  │")
    print("   └─────┴─────┴─────┘")
    print()
    print(f"{player1_name} играет - X\n")
    print(f"{player2_name} играет - O\n")
    return


# Функция анализа всех лиий игрового поля и определения ситуаций выигрыша или ничьей, а также подсчёта сумм всех линий и макс и мин значений линий и ключей этих линий
def count_lines():
    global fields_dict, lines_dict, lines_sums
    global max_line_sum, min_line_sum, max_line_key, min_line_key

    lines_sums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    max_line_sum = lines_sums[1]
    max_line_key = 1
    min_line_sum = lines_sums[1]
    min_line_key = 1

    draw = True

    for lkey in lines_dict.keys():
        for field_name in lines_dict[lkey]:
            if fields_dict[field_name] == 0:
                draw = False
            lines_sums[lkey] += fields_dict[field_name]
        if max_line_sum < lines_sums[lkey]:
            max_line_sum = lines_sums[lkey]
            max_line_key = lkey
        if min_line_sum > lines_sums[lkey]:
            min_line_sum = lines_sums[lkey]
            min_line_key = lkey
    if min_line_sum == -3:
        return 2
    elif max_line_sum == 3:
        return 1
    elif draw:
        return -1
    return 0


# Функция хода игрока. 0 - аварийный выход из программы.
def player_move(player):
    global player1_turn, player1_inc, player1_name, player2_inc, player2_name
    global fields_dict

    if player1_turn:
        player = player1_name
    else:
        player = player2_name

    if player == "Компьютер" or "бот" in player:
        field_to_move = pc_logic()
    else:
        while True:
            field_to_move = input(f"{player}, укажите поле для хода: ")
            if field_to_move not in ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', "0"]:
                print("Вы неправильно указали поле. Попробуйте ещё раз")
            elif fields_dict[field_to_move] != 0:
                print("Это поле уже занято. Укажите другое")
            else:
                break

    if field_to_move == 0:
        exit()

    if player1_turn:
        fields_dict[field_to_move] += player1_inc
        player1_turn = False
    else:
        fields_dict[field_to_move] += player2_inc
        player1_turn = True

    return


# Функция логики бота
def pc_logic():
    global player1_turn
    global fields_dict, lines_dict
    global max_line_sum, min_line_sum, max_line_key, min_line_key

    time.sleep(1)

    first_move = True

    for field in fields_dict.values():
        if field != 0:
            first_move = False
            break

    if player1_turn and not first_move:
        if max_line_sum >= -min_line_sum:
            for fkey in lines_dict[max_line_key]:
                if fields_dict[fkey] == 0:
                    return fkey
        elif max_line_sum < -min_line_sum:
            for fkey in lines_dict[min_line_key]:
                if fields_dict[fkey] == 0:
                    return fkey
    elif not player1_turn and not first_move:
        if -min_line_sum >= max_line_sum:
            for fkey in lines_dict[min_line_key]:
                if fields_dict[fkey] == 0:
                    return fkey
        elif -min_line_sum < max_line_sum:
            for fkey in lines_dict[max_line_key]:
                if fields_dict[fkey] == 0:
                    return fkey
    while True:
        random_key = random.choice(
            ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3'])
        if fields_dict[random_key] == 0:
            break
    return random_key


# Функция инициализации новой игры
def game_init():
    global player1_name, player2_name

    print("Добро пожаловать в игру Крестики - нолики!\n")
    print(f"Выберите, кто будет играть?\n 1 - человек vs человек\n 2 - человек vs компьютер\n")

    while True:
        try:
            play_mode = int(input("Введите цифру: "))
            if play_mode not in [1, 2, 9]:
                print("Вы ввели неправильное значение, попробуйте ещё раз\n")
            else:
                break
        except ValueError:
            print("Вы ввели неправильное значение, попробуйте ещё раз\n")

    print()

    if play_mode == 1:
        temp_player1_name = input("Как зовут игрока 1? - ")
        temp_player2_name = input("Как зовут игрока 2? - ")
    elif play_mode == 2:
        temp_player1_name = input("Как зовут игрока? - ")
        temp_player2_name = "Компьютер"
    else:
        temp_player1_name = "бот Николай"
        temp_player2_name = "бот Константин"

    clear()

    print("\nЧто ж, бросаем жребий, кто ходит первым\n")
    time.sleep(1)

    if random.randint(1, 2) == 1:
        player1_name = temp_player1_name
        player2_name = temp_player2_name
        print(f"{player1_name} ходит первым")
    else:
        player1_name = temp_player2_name
        player2_name = temp_player1_name
        print(f"{player1_name} ходит первым")
    time.sleep(2)
    print("\nИгра началась\n")

    return


# Старт программы
clear()
game_init()
is_over = 0

while True:
    print_field()
    is_over = count_lines()
    if is_over != 0:
        if is_over == -1:
            print(f"Победила дружба! НИЧЬЯ!!!\n")
        elif is_over == 1:
            print(f"Победил {player1_name}! УРА!!!\n")
        else:
            print(f"Победил {player2_name}! УРА!!!\n")
        break
    if player1_turn:
        player_move(1)
    else:
        player_move(2)

print("\nGAME OVER!\n")


# решение https://github.com/Alisbur/Python_Examples/commit/a849646c207e3250d3640d50830a2227dbb051ae