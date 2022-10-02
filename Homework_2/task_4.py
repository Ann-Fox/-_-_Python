# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


from random import random

number = int(input("Введите размер списка: "))
# number_list = list(range(1, number+1))
number_list = []

for i in range(0, number):
    number_list.append(int(random()*2*number-number))
print(number_list)
