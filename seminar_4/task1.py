# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# slip(' ') == slip() -> список строк/чисел -> найти max и min

# вариант (семинар Святослав) чтение файла
file_path = r'seminar_4\file1.txt'
# f = open(file_path, 'a')
with open(file_path, 'r') as f:
    str_list = f.read()
    # print(str_list)

str_list = str_list.split()

for i in range(len(str_list)):
    str_list[i] = int(str_list[i])
print(str_list)

print(max(str_list))


# вариант 1 (семинар Альбина)
# list_num = [int(i) for i in input("Введите числа через пробел: ").split()]

# max_num = max(list_num)
# min_num = min(list_num)

# print(f"Максимальное число -> {max(list_num)}, минимально число -> {min(list_num)}")
