import os
def clear(): return os.system('cls')
import datetime


SOURCE_PATH = "tasc.csv"

def log_in(operation, op1, op2, result):
    b = datetime.datetime.now()
    with open(SOURCE_PATH, 'a', encoding="UTF-8") as source: 
        source.write(f"{b.strftime('%Y-%m-%d-%H.%M.%S')} - {operation} - {op1} - {op2} - {result} \n")
    return 0

def log_out():
    with open(SOURCE_PATH, "r", encoding="UTF-8") as source: 
        for line in source:
            print(line, end="")
    return 0

def num_input():
    while True:
        try:
            imag = float(input("Введите мнимую часть: "))
            break
        except ValueError:
            print("Неверный ввод. Попробуйте еще раз")
    while True:
        try:
            real = float(input("Введите вещественную часть: "))
            break
        except ValueError:
            print("Неверный ввод. Попробуйте еще раз")
    return [real, imag]

def calc(operation, op1, op2):

    c1 = complex(op1[0], op1[1])
    c2 = complex(op2[0], op2[1])

    if operation == 1:
        res = c1 + c2
    elif operation == 2:
        res = c1 - c2
    elif operation == 3:
        res = c1 * c2
    else:
        res = c1/c2
    return [res.real, res.imag]


def menu():

    operation = 0

    print("Программа - Калькулятор \n")
    print("1. Сложение чисел ")
    print("2. Вычитание чисел")
    print("3. Умножение чисел")
    print("4. Деление чисел")
    print("9. Лог событий \n")
    print("0. Выход \n")

    while True:
        try:
            point = int(input("Введите номер пункта меню: "))
            if point in [1, 2, 3, 4, 9, 0]:
                break
        except ValueError:
            print("Введен неправильный пункт меню. Попробуйте еще раз")


    if point in [1, 2, 3, 4]:
        operation = point
    elif point == 9:
        log_out()
        return
    else:
        exit()

    operand1 = num_input()
    operand2 = num_input()

    result = (calc(operation, operand1, operand2))
    print(result)
    log_in(operation, operand1, operand2, result)

    return


while True:
    menu()
    clear()

# while True:
#     try:
#         num1 = float(input("Введите операнд 1: "))
#         break
#     except ValueError:
#         print("Введен неправильный пункт меню. Попробуйте еще раз")

# while True:
#     try:
#         num1 = float(input("Введите операнд 2: "))
#         break
#     except ValueError:
#         print("Введен неправильный пункт меню. Попробуйте еще раз")


