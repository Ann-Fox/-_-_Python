# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
import math
import numpy

a = int(input("Введите А: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))

# 1. с помощью математических формул нахождения корней квадратного уравнения

discriminant = b**2 - 4*a*c
print('Дискриминант = ' + str(discriminant))

if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))

# 2. с помощью дополнительных библиотек Python (например, numpy.roots)
p = [a, b, c]
print(f"{numpy.roots(p)}")
