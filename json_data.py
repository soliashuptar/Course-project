import json


def read_data(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            station = line[3]
            date = line[6]
            time = line[7]
            entrances = line[9]
            exits = line[10]
            coords = [line[11], line[12]]
            info = {
                'station': station,
                'date': date,
                'time': time,
                'entrances': entrances,
                'exits': exits,
                'coords': coords
            }
            yield info


def write_data(filename, data):
    with open(filename, 'a') as file:
        json.dump(data, file)


data_gen = read_data('data.txt')

DATA = {
    'info': []
}




for i in range(10):
    DATA['info'].append(next(data_gen))
    print("SDSS")

write_data('newdata.json', DATA)


