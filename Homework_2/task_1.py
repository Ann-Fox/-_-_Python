# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

real_number = input("Введите вещественное число real_number: ")

result = 0
for i in real_number:
    if i != '.':
        result += int(i)
print(f'{real_number} -> {result}')
