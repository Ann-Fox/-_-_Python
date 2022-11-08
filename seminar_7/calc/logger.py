# Модуль 2: логирование

from datetime import datetime as dt
from time import time


def math_oper_logger(data = 0):
    time = dt.now().strftime('%H:%M')
    with open('d:\Seminar\seminar_7\calc\log.csv', "a") as file:
        file.write('{};{}\n'
                   .format(time))
    # with open('log.csv','r') as f:
    #     f = file.read()
        # print(f)
    return time

math_oper_logger()



# def logg(head='INFO', body='Start program'):
# log_path = Path('data', 'logging.txt')
# log_time = datetime.now().strftime("%Y-%M-%d | %H:%M:%S | ")
# with open(log_path, 'a') as log:
# text = f'{(head + ":"):7}{log_time:30}{body}\n'
# log.write(text)