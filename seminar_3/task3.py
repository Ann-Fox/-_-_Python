# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time

# def find_time(x):
#     a = str(time.time())
#     b = ''
#     count = 1
#     while count <= x:
#         b += a[-count]
#         count += 11
#     print(int(b))

# find_time(5)


# super
l = int(input('Введите длину числа: '))

ms = int(((time.time() % 1)*(10**(l+1))) % (10**(l)))
# ms=time.time()
# ms=int(time.time()%10)

print(ms)
