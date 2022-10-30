# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# disc
# x1, x2

path = r'seminar_4\file2.txt'
with open(path, 'r') as my_file:
    data = my_file.read()

data = data.split()
print(data)
data = data[:-2]
print(data)
data = [int(data[0][:-3]), int((data[1]+data[2])[:-1]), int(data[3]+data[4])]
print(data)

a = '-3x'
a = a[:-1]
print(a)

# D=b**2-4dc
d = data[1]**2-4*data[0]*data[2]
print(d)

# x=((-b+(d^(1/2)))/(2*a))
x_1=(-data[1]+d**0.5)/(2*data[0])
x_2=(-data[1]-d**0.5)/(2*data[0])
print(x_1, x_2)





# data = open('ert.txt', 'w')

# data.writelines('\nLesson 5')

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))

# d = b**2-4*c*a
# x1 = (-b+d**0.5)/(2*a)
# x2 = (-b-d**0.5)/(2*a)

# data.writelines(f'\n {a}*x^2+{b}*x+{c}=0 \nx1 = {x1}, \nx2 = {x2}')
# data.close




# import math
# import numpy

# a = int(input("Введите А: "))
# b = int(input("Введите B: "))
# c = int(input("Введите C: "))

# 1. с помощью математических формул нахождения корней квадратного уравнения

# discriminant = b**2 - 4*a*c
# print('Дискриминант = ' + str(discriminant))

# if discriminant < 0:
#     print('Корней нет')
# elif discriminant == 0:
#     x = -b / (2 * a)
#     print('x = ' + str(x))
# else:
#     x1 = (-b + discriminant ** 0.5) / (2 * a)
#     x2 = (-b - discriminant ** 0.5) / (2 * a)
#     print('x₁ = ' + str(x1))
#     print('x₂ = ' + str(x2))

# 2. с помощью дополнительных библиотек Python (например, numpy.roots)
# p = [a, b, c]
# print(f"{numpy.roots(p)}")
