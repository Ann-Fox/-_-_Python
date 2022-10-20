def get_output_CSV():
    flag = True
    with open('data_tel.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            if not line == '\n':
                line = line.strip()
                line = line + '; '
                if flag:
                    with open('data_tel.csv', 'w', encoding='UTF-8') as f_:
                        f_.write(line)
                        flag = False
                else:
                    with open('data_tel.csv', 'a', encoding='UTF-8') as f_:
                        f_.write(line)
            else:
                with open('data_tel.csv', 'a', encoding='UTF-8') as f_:
                    f_.write('\n')


get_output_CSV()
