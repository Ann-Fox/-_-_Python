# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# 12 --> ['abc12', '12','asb','87'] --> 'abc12', '12'

# my_list = ['abc12', '12','asb','87','8','5','fds123']
# for i in my_list:
#     if '12' in i:
#         print(i)


# оптимизация
my_list = ['abc12', '12','asb','87','8','5','fds123']

def search(x):
    for i in x:
        if '12' in i:
            print(i)

search(my_list)