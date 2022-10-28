# 3.	Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# function
# st1 = 'hello, world!'
# st2 = ','

# def str(s1, s2):
#     count = 0
#     for i in range(len(s1)-len(s2)):
#         if (s1[i: i + len(s2)] == s2):
#             count += 1
#     print(count)


# str(st1, st2)

# while
# symbol = "so"
# base_str = "some personal ..."
# position=0
# count = 0
# while (True):
#     position = base_str.find(symbol, position)
#     if position == -1:
#         break
#     else:
#         position += 1
#         count+=1
# print(count)


# count 
def find_line(string:str, under_string:str):
    print(string.count(under_string))

user_string = input('Введите текст: ')
user_understring = input('Введите текст: ')
find_line(user_string, user_understring)


# textFirst = input('Введите первую строку: ')
# textSecond = input('Введите вторую строку: ')

# string = ''
# subString = ''

# if len(textFirst) > len(textSecond):
#     string = textFirst
#     subString = textSecond
# else:
#     string = textSecond
#     subString = textFirst

# print(string.count(subString))

# count = 0
# counter = 0

# for i in range(len(string) - len(subString)):
#     if string[i] == subString[0]:
#         counterIn = 0
#         for k in range(len(subString)):
#             if subString[0+k] == string[i+k]:
#                 counterIn += 1
#         if counterIn == len(subString):
#             counter += 1

# print(f'Counter = {counter}')
