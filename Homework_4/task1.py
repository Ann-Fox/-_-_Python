# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# Можно округлить пи из math, там точность 15 знаков

import math

num = int(input(f'Сколько цифр должнобыть после запятой: '))
pi = round((math.pi), num)
print(f'{pi}')


# def calc_factor(num):
#     result = 0
#     while num % 1 > 0:
#         num *= 10
#         result += 1
#     return result


# fract_accur = float(input("ВВедите необходимую точность: "))
# roun_pi = round(math.pi, calc_factor(fract_accur))
# print(roun_pi)
