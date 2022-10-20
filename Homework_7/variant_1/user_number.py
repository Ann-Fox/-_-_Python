

def get_user_number(str_1, list_user):
    while True:
        try:
            num = int(input(str_1))
            if num in list_user:
                return num
            else:
                print('Что-то пошло не так. Повторите ввод')
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
