# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))



# fib1 = fib2 = 1
 
# n = int(input())
 
# print(fib1, fib2, end=' ')
 
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')




# num_n = int(input("сколько чисел фибоначчи вывести?: "))
# list_num = []
# temp = 0
# count = 0
# for i in range(0, num_n+1):
#     list_num.append(temp)
#     if temp == 0:
#         temp = 1
#     temp += list_num[i-1]
# negativ_list = []
# count = len(list_num)-1
# j = 0
# for i in range(len(list_num)):
#     if list_num[i] != 0 and i%2 == 0:
#         negativ_list.append(list_num[i]*-1)
#     elif i%2 != 0:
#         negativ_list.append(list_num[i])
# negativ_list = negativ_list[::-1]
# negativ_list.extend(list_num)

# print(negativ_list)