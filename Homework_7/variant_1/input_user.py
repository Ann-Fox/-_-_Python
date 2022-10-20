import user_number as un
import record_file as rf


def get_data_abonent(field_print, msg, n=True):
    data_user = '-' * (field_print + 1)
    while len(data_user) > field_print:
        data_user = input(msg)
        data_user = data_user.strip()
        if data_user == '':
            data_user = '-'
    if n:
        return data_user + (field_print - len(data_user)) * ' '
    else:
        return data_user


def get_input_user():
    print()
    print('-------------------------')
    print('  ТЕЛЕФОННЫЙ  СПРАВОЧНИК')
    print('   ввод нового телефона')
    print('-------------------------')

    name = get_data_abonent(40, 'Введите ИМЯ (не более 30 символов): ')
    tel = get_data_abonent(20, 'Введите ТЕЛЕФОН (не более 20 символов): ')
    note = get_data_abonent(60, 'Введите ПРИМЕЧАНИЕ: ', False)

    print('-------------------------')
    while True:
        print('-------------------------')
        print('Имя: ', name)
        print('Телефон: ', tel)
        print('Примечания: ', note)
        print('-------------------------')

        x = input('Все верно? (Д, Нет): ')
        x = x.strip().lower()
        if x == 'д' or x == 'y' or x == '':
            rf.get_record_file(name, tel, note)
            return
        else:
            print('-----------------------------')
            print('Корректировка вводимых данных')
            print('-----------------------------')
            print('1 - имя')
            print('2 - телефон')
            print('3 - примечание')
            print('4 - я передумал, все верно')
            print('-----------------------------')
            num_user = un.get_user_number(
                'Какую операцию выполняем? - ', [1, 2, 3, 4])
            if num_user == 1:
                name = input('Введите ИМЯ: ')
            if num_user == 2:
                tel = input('Введите ТЕЛЕФОН: ')
            if num_user == 3:
                note = input('Введите ПРИМЕЧАНИЕ: ')
            if num_user == 4:
                rf.get_record_file(name, tel, note)
                return
