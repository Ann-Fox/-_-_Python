def get_user_number(str_1, list_user):
    while True:
        try:
            num = int(input(str_1))
            if num in list_user:
                return num
            else:
                print('Неверный ввод, повторите, пожалуйста')
        except ValueError:
            print('Неверный символ, введите число')
