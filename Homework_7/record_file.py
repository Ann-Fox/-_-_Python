def get_record_file(n, t, nt):
    with open('data_tel.txt', 'a', encoding="UTF-8") as f:
        f.write(f'{n}\n')
        f.write(f'{t}\n')
        f.write(f'{nt}\n')
        f.write('\n')
