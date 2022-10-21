def get_add_user(data: list) -> list:
    if not data:
        user: dict = {}
        user['фио'] = input('Введите фио: ')
        user['фио'] = user['фио'].title()
    else:
        sample = data[0]
        user = {}
        for i in sample:
            user[i] = input(f'Введите {i}: ')
            if i == 'фио':
                user[i] = user[i].title()
            else:
                user[i] = user[i].capitalize()
    data.append(user)
    return data