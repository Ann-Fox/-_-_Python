def get_print_user_all(data):
    print('Персональные данные сотрудников\n')
    for user in data:
        for key, value in user.items():
            print(f'{key}: {value}')
        print('_________________________')
    input('Для выхода в меню нажмите Enter')

def get_print_user_for_one(data):
    print('Персональные данные сотрудников\n')
    for user in data:
        for key, value in user.items():
            print(f'{key}: {value}')
        what  = input ('Внести изменения?:\n(нет - Enter, да - д, вернуться в главное меню - м)\n')
        if what == 'м':
            for key, value in user.items():
                print(f'{key}: {value}')
                item=input(f'{key}, внести изменения?\n'
            '(нет - Enter, да - д): ')
                if item == 'д':
                    user[key] = input(f'{key}: ')
                    if key == 'фио':
                        user[key]=user[key].title()
        elif what == 'м':
            return data
    return data
