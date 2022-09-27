# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_week = int(input("Введите число day of the week "))
match day_week:
  case 1:
    print(f'{day_week} -> No')
  case 2:
    print(f'{day_week} -> No')
  case 3:
    print(f'{day_week} -> No')
  case 4:
    print(f'{day_week} -> No')
  case 5:
    print(f'{day_week} -> No')
  case 6:
    print(f'{day_week} -> Yes')
  case 7:
    print(f'{day_week} -> Yes')
  case _:
    print('Вы ввели некорректное число')
