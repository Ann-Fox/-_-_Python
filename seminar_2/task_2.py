# 2.	Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {
# 1: 4, 
# 2: 7, 
# 3: 10, 
# 4: 13, 
# 5: 16, 
# 6: 19}

Number_N = int(input("Введите число: "))
print(f"Number_N = {Number_N}: ", end = " ")

for i in range(1, Number_N+1):
  print(f"{i}:{3*i+1}", end = " ")


# Number = int(input("Введите число N:"))
# sumN = 1
# count = 0
# while count <= Number:
#     count += 1
#     sumN = 3*count+1
    
#     print(sumN)



# n = int(input('введите число: '))
# list = []
# for i in range(1, n + 1):
#     list.append(f"{i} : {3 * i + 1}")
# print(", ".join(list))


Number = int(input('введите чимло N: '))

result = {}
for key in range(1, Number+1):
  result[key] = key*3+1

print(result)