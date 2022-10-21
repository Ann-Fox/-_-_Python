import os
import menu
import creat_base as cb
import add_key as ak
import add_user as us
import print_user as pu

def clear(): return os.system('cls')

def data_comm():
    exit = True
    data_flag = False
    data = cb.read_file("Homework_8\data_base.json")
    if data == []:
        data_flag = True
    while exit:
        if data_flag:
            what = 3
            data_flag = False
        else:
            what = menu.menu()
        if what == 1:
            clear()
            pu.get_print_user_for_one(data)
            cb.write_file(data)
            clear()
        elif what == 2:
            clear()
            pu.get_print_user_all(data)
            clear()
        elif what == 3:
            clear()
            us.get_add_user(data)
            cb.write_file(data)
            clear()
        elif what == 4:
            clear()
            ak.get_add_key(data)
            cb.write_file(data)
            clear()
        else:
            cb.write_file(data, "Homework_8\data_base_2.json")
            exit = False


data_comm()
