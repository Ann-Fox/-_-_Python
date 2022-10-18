# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'абв1111 qwerty555 абв1111 qwert'
my_list = my_str.split(' ')
res = ""
for word in my_list:
    if 'абв' not in word:
        res += word + " "
print(res.strip())  # обрезает пробел, табулятор



# вариант 2
my_str2 = 'qpoiu абв1111 qwerty555 абв1111 qwert'
my_list2 = my_str2.split(' ')
res2 = []
for words in my_list2:
    if "абв" not in words:
        res2.append(words)
print(" ".join(res2))  


