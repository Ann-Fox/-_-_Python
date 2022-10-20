import os


import user_number as un
import input_user as i_u


def menu():
    print()
    print('-------------------------')
    print('  ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    print('-------------------------')
    print('1 - поиск (пока не работает)')
    print('2 - вывод всех абонентов')
    print('3 - ввод нового телефона')
    print('4 - исправление записи (пока не работает)')
    print('5 - вывод базы в HTML')
    print('6 - вывод базы в CSV')
    print('0 - выход')
    print('-------------------------')
    num_user = un.get_user_number(
        'Какую операцию выполняем? - ', [1, 2, 3, 4, 5, 6, 0])
    return num_user
