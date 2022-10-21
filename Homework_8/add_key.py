def get_add_key(data):
    user = input('Введите название нового поля: ')
    for x in data:
        if not x == data[0]:
            x[user] = '*'
        else:
            print(x['фио'])
            x[user] = input('Введите значение: ')
    return data