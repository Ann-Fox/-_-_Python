# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

num_list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = []
new_list.append(num_list[0])
max_num = num_list[0]
for i in range(1, len(num_list)):
    if num_list[i] > max_num:
        new_list.append(num_list[i])
        max_num = num_list[i]

print(new_list)

# вариянт 2
# my_list = [1, 5, 2, 5, 8, 2, 5, 7]
# result = []
# count = 0
# result.append(my_list[0])

# for i in my_list:
#     if i > result[count]:
#         result.append(i)
#         count += 1

# print(result)


# вариянт 2
my_list = [1, 5, 2, 5, 8, 2, 5, 7]
result = []
result.append(my_list[0])

for i in my_list:
    if i > result[-1]:
        result.append(i)
    
print(result)