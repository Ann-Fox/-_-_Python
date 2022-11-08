import random


#Вывод поля
#Определение очередности хода
#Ход или принятие



# Глобальные переменные параметров игры
player1_turn = True
player1_inc = 1
player1_name = "Игрок 1"
player2_inc = -1
player2_name = "Игрок 2"

# Глобальные словари всех полей, линий и сумм линий
fields_dict = {}
lines_dict = {}
lines_sums = {}

# Глобальные переменные макс и минимальных значений линий и их ключей в словаре
max_line_sum = 0
min_line_sum = 0
max_line_key = 1
min_line_key = 1


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
        return 2    #Выиграли 0
    elif max_line_sum == 3: 
        return 1    #Выиграли X
    elif draw:
        return -1   #Ничья
    return 0        #Игра продолжается


def player_move(field):
    global player1_turn, player1_inc, player1_name, player2_inc, player2_name
    global fields_dict


    if player1_turn:
        field_to_move = field
    else:
        field_to_move = pc_logic()

    if player1_turn:
        fields_dict[field_to_move] += player1_inc
        player1_turn = False
    else:
        fields_dict[field_to_move] += player2_inc
        player1_turn = True
    
    return count_lines()


# Функция логики бота
def pc_logic():
    global player1_turn
    global fields_dict, lines_dict
    global max_line_sum, min_line_sum, max_line_key, min_line_key

    first_move = True
    second_move = False

    for field in fields_dict.values():
        if field != 0:
            first_move = False
            second_move = True
            break

    if fields_dict["B2"] == 0:
        return "B2"

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



def print_field(player_sym):
    global fields_dict, player1_name, player2_name

    if player_sym == "X":
        comp_sym = "O"
    else:
        comp_sym = "X"

    xo_dict = {}
    for fkey in fields_dict.keys():
        if fields_dict[fkey] == 0:
            xo_dict[fkey] = f"/{fkey}"
        elif fields_dict[fkey] == -1:
            xo_dict[fkey] = "  "+comp_sym+"  "
        else:
            xo_dict[fkey] = "  "+player_sym+"  "
    
    result_str = ""

    result_str += f"│ {xo_dict['A1']} │ {xo_dict['B1']} │ {xo_dict['C1']} │\n"
    result_str += f"│ {xo_dict['A2']} │ {xo_dict['B2']} │ {xo_dict['C2']} │\n"
    result_str += f"│ {xo_dict['A3']} │ {xo_dict['B3']} │ {xo_dict['C3']} │"

    return result_str



def game_init():
    global player1_name, player2_name, player1_turn
    global fields_dict, lines_dict, lines_sums
    global max_line_sum, min_line_sum, max_line_key, min_line_key

    fields_dict = {'A1': 0, 'B1': 0, 'C1': 0, 'A2': 0, 'B2': 0, 'C2': 0, 'A3': 0, 'B3': 0, 'C3': 0}
    lines_dict = {1: ('A1', 'A2', 'A3'), 2: ('B1', 'B2', 'B3'), 3: ('C1', 'C2', 'C3'), 4: ('A1', 'B1', 'C1'), 5: ('A2', 'B2', 'C2'), 6: ('A3', 'B3', 'C3'), 7: ('A1', 'B2', 'C3'), 8: ('A3', 'B2', 'C1')}
    lines_sums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    max_line_sum = 0
    min_line_sum = 0
    max_line_key = 1
    min_line_key = 1

    # player1_turn = True

    # return "X"

    if random.randint(1, 2) == 1:
        player1_turn = True
        return "X"
    else:
        player1_turn = False
        player_move("A1")
        return "O"