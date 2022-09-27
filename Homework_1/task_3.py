# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coordinate_x = int(input('Введите координату X '))
coordinate_y = int(input('Введите координату Y '))

if (coordinate_x > 0 and coordinate_y > 0):
  print(f"x = {coordinate_x}; y = {coordinate_y} -> 1")
if (coordinate_x < 0 and coordinate_y > 0):
  print(f" x = {coordinate_x}; y = {coordinate_y} -> 2")
if (coordinate_x < 0 and coordinate_y < 0):
  print(f"x = {coordinate_x}; y = {coordinate_y} -> 3")
if (coordinate_x > 0 and coordinate_y < 0):
  print(f"x = {coordinate_x}; y = {coordinate_y} -> 4")