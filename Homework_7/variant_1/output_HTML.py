
def get_output_HTML():
    with open('data_tel.html', 'w', encoding='UTF-8') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="ru">\n')
        f.write('<head>\n')
        f.write('<meta charset="UTF-8">\n')
        f.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
        f.write('<meta name="viewport" content="width='
                'device-width, initial-scale=1.0">\n')
        f.write('<title>ТЕЛЕФОННЫЙ СПРАВОЧНИК</title>\n')
        f.write('</head>\n')
        f.write('<body style="font-size: 16px;">\n')

    with open('data_tel.txt', 'r', encoding='UTF-8') as f:
        count = 1
        for line in f:
            if not line == '\n':
                line = line.strip()
                with open('data_tel.html', 'a', encoding='UTF-8') as f_:
                    if count == 1:
                        f_.write(
                            f'<p style="margin: 0px;">Имя: <b style="font-size: 20px;">{line}</b></p>\n')
                    elif count == 2:
                        f_.write(
                            f'<p style="margin: 0px;">Телефон: <b style="font-size: 20px;">{line}</b></p>\n')
                    elif count == 3:
                        f_.write(
                            f'<p style="margin: 0px;">Примечание: <b style="font-size: 20px;">{line}</b></p>\n')
                    count += 1
                    if count == 5:
                        count = 1
            else:
                with open('data_tel.html', 'a', encoding='UTF-8') as f_:
                    f_.write('<hr>\n')
                    count += 1
                    if count == 5:
                        count = 1
    with open('data_tel.html', 'a', encoding='UTF-8') as f_:
        f_.write('</body>\n')
        f_.write('</html>')


get_output_HTML()
