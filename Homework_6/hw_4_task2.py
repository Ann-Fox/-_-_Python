# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return primfac

natural_number = int(input("Введите натуральное число: "))
res = primfacs(natural_number)
print(res)

# num = int(input("Введите число: "))
# mult = 2
# list_mult = []
# while num > mult:
#     if (num % mult == 0):
#         list_mult.append(mult)
#         num /= mult
#         mult = 2
#     else:
#         mult += 1
# print(list_mult)
