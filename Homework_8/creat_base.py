import json
import os


def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf8') as read_file:
            data = json.load(read_file)
    else:
        data = []
        print('\n'
              'Информационная система компании GRAPH\n'
              'Введите данные первого сотрудника\n')
    return data


def write_file(data, file_reserve='Homework_8\data_base.json'):
    with open(file_reserve, 'w', encoding='utf8') as write_file:
        json.dump(data, write_file, ensure_ascii = False, indent = 4)
