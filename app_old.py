# Pobierz z pliku tekstowego listę osób i wypisz te osoby, które
# są pełnoletnie.

try:
    data = open('people.txt')
    data_list = []
    for i in data:
        data_line = i[:-1]
        ostatni_srednik = data_line.rindex(';')
        w = int(data_line[ostatni_srednik + 1:])
        if w > 18:
            print(data_line)
    data.close()
except:
    print('File error')