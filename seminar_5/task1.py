# 1. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.




# вариант 1
# num_list = [1, 2, 3, 4, 5, 7, 8, 9]
# print(num_list)

# for i in range(1, len(num_list)):
#     if not num_list[i] - 1 == num_list[i - 1]:
#         print(f'В файле не хватает числа {num_list[i] - 1}')


# вариант 2
# number = []

# path = 'seminar_5\file.txt'
# date = open(path, 'r')
# line = date.read()
# date.close()

# print(line)

# for i in line.split():
#     number.append(int(i))
# print(number)
# count = number[0]
# for i in range(1, len(number)):
#     count += 1
#     if number[i] == count:
#         continue
#     else:
#         print(f'Нет числа {count}')
