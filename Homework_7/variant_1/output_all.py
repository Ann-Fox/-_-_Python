

def get_output_all():
    with open('data_tel.txt', 'r', encoding="UTF-8") as f:
        print('-' * 80)
        for line in f:
            if not line == '\n':
                line = line.replace('\n', '')
                print(line, end=' ')
            else:
                print('')
                print('-' * 80)
