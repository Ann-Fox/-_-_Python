# my_list = '1 22 54 76 2'.split()
# print(my_list)
# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i])
# print(my_list)


# включения, улучшение кода

my_str = '1 22 54 76 2'.split()
# что делать с эелементом, с каким элементом, условие
# my_list = [int(my_str[i]) for i in range(len(my_str))]

# еще улучшили
# my_list = [int(item) for item in my_str]

# условие, не выполняется ошибка
# my_list = [int(item) for item in my_str if (item > 10)]
my_list = [int(item) for item in my_str]
print(my_list)


# лямбда
def f():
    pass


def f():
    ...


def f(x): return x**2 if x > 10 else x**3
# print(f(12))


my_list = [12, 54, 3, 65]

res = list(map(f, my_list))
print(res)

res = tuple(map(f, my_list))
print(res)


# filter
f = lambda x: True if x > 10 else False
my_list = [12, 54, 3, 65]
res = list(filter(f, my_list))
print(res)


# zip
f = lambda x: True if x > 10 else False
my_list_1 = ['f', 'j', 'k', 't']
my_list_2 = [12,64, 1, 98]
my_list_3 = [65, 68, 85]

res = list(zip(my_list_1, my_list_2, my_list_3))
print(res)


# enumerate
my_list_1 = ['f', 'j', 'k', 't']
res = list(enumerate(my_list_1))
print(res)


# data = list(map(int, input().split()))


# удалить из исходной строки все слова с "абв"
str_list = 'Привет, Мир! Мы очабв Пайтонабв! Семинары'
# str_list = str_list.split()
# print(str)

# def strs(str):
#     for item in str_list:
#         if 'абв' in item:
#             str_list.remove(item)
#     print(str_list)
# strs(str_list)

# оптимизация
res = list(filter(lambda item: 'абв' not in item, str_list.split()))
print(res)


#  
my_str = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# найти слова в словах в строке, при условии что это слово не содержится в слове
res = [word for word in my_str.split() if 'абв' not in word]
print(' '.join(res))

