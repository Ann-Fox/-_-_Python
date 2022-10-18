# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# вариянт 1
numbers = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8]

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(get_unique_numbers(numbers))

# вариант 2

# list_inp = [100, 75, 100, 20, 75, 12, 75, 25]

# set_res = set(list_inp)
# print("список неповторяющихся элементов исходной последовательности:\n")
# list_res = (list(set_res))

# for item in list_res:
#     print(item)

# вариант 3 Альбина
# from itertools import count
# from typing import Counter

# nums = input('Введите числа через пробел: ').split()
# counts = {}
# for i in nums:
#     if i not in counts:
#         counts[i] = 0
#     counts[i] += 1
# res = []
# for key in counts:
#     if counts[key] == 1:
#         res.append(int(key))
# print(res)


# вариант 4 Альбина
# nums = input('Введите числа через пробел: ').split()
# counts = Counter(nums)
# print([i for i in counts if count[i] == 1])