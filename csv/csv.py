import csv
from main import Products


def read_csv():
    with open('new.csv', 'r') as file:
        x = csv.DictReader(file)
        data = list(x)
        return data


def append_csv(filename, data):
    with open(filename, 'a') as file:
        file.write(f'{data}\n')


def write_csv(filename):
    with open(filename, 'w') as f:
        f.write('name,price,quantity,total\n')


write_csv(filename='data1.csv')
for i in read_csv():
    append_csv('data1.csv',
               f"{i.get('name')},"
               f"{i.get('price')},"
               f"{i.get('quantity')},"
               f"{float(i.get('price')) * int(i.get('quantity'))}")
