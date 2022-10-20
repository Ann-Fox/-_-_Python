import menu
from input_user import get_input_user
from output_all import get_output_all
from output_CSV import get_output_CSV
import output_HTML as oh


def get_start():
    exit = True
    while exit:
        what = menu.menu()
        if what == 1:
            # get_search()
            exit = False
        elif what == 2:
            get_output_all()
            print()
            input('Для продолжения нажмите Enter')
            # exit = False
        elif what == 3:
            get_input_user()
        elif what == 4:
            # get_correction_user()
            exit = False
        elif what == 5:
            oh.get_output_HTML()
            print()
            print('Операция 5 осуществленна. Создан файл: data_tel.html')
        elif what == 6:
            get_output_CSV()
            print()
            print('Операция 6 осуществленна. Создан файл: data_tel.csv')
        else:
            exit = False
