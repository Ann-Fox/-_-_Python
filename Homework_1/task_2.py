# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(
                f'x={x}, y={y}, z={z}, ¬(X ⋁ Y ⋁ Z) = {not(x or y or z)},   ¬X ⋀ ¬Y ⋀ ¬Z = {not (x) and not (y) and not (z)} ')




# trigger = True

# for x in [True, False]:
#   for y in [True, False]:
#     for z in [True, False]:
#       if not(x or y or z) != (not x) and (not y) and (not z):
#         print('False')
#         trigger = False
#         break

# if trigger: print('Выражение верно')               