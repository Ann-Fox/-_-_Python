# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


# решение: https://github.com/Alisbur

source_str = "оаааа тттпло лыааббббвва ывлллллллллллабвввдо ывдлыыыыытпл ывдддалт ыввл"
words_list = source_str.split(" ")
result_word = ""
result_list = []
counter = 0

for word in words_list:
    result_word = word[0]
    for ch in word:
        if result_word[-1] == ch:
            counter += 1
        else:
            result_word += str(counter)
            result_word += ch
            counter = 1
    result_word += str(counter)
    result_list.append(result_word)
    counter = 0

print(" ".join(result_list))