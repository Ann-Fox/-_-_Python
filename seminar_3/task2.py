# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# my_list = ['qwe', 'asd', 'zxc', 'qwe', 'qweasd']

# count = 0
# for i in my_list:
#     if i in my_list:
#         if 'qwe' in i:
#             count += 1
#             if count > 1:
#                 print(f"{my_list} --> qwe --> {i}")
#             else:
#                 print(-1)


# range
my_list = ['qwe', 'asd', 'zxc', 'qwe', 'qweasd', 'qwe']

count = 0
for i in range(len(my_list)):
    if my_list[i] == 'qwe':
            count += 1
            if count > 1:
                print(f"{my_list} --> qwe --> {i}")
                break
