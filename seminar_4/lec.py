# r - чтение
# w - запись
# a - создание и дозапись

# a - создание, добавление, add
# file_path = r'seminar_4\file-lec.txt'
# f = open(file_path, 'a')
# f.close()

# file_path = r'seminar_4\file-lec.txt'
# f = open(file_path, 'a')     # открытие
# f.write('\n123\n')           # дозапись
# print(f.read())
# f.close()


# если забываем закрыват файл командой close() 
file_path = r'seminar_4\file-lec.txt'
with open(file_path, 'w') as f:
    f.write('asdf')


# r - чтение, read
# file_path = r'seminar_4\file-lec.txt'
# f = open(file_path, 'r')
# print(f.read())              #можно передать количество символов
# f.close()

# file_path = r'seminar_4\file-lec.txt'
# f = open(file_path, 'r')
# for line in f:
#     print(line, end='')                     # построчно считывает файл
# f.close()


# w - запись, write, создать/перезаписать файл, использовать осторожно
# file_path = r'seminar_4\file-lec.txt'
# f = open(file_path, 'w')
# f.write("asdf 1233 123")
# f.close()

