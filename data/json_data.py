import json
# import os


# os.listdir()
def read_data(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            info = {
                'station': line[3],
                'date': line[6],
                'time': line[7],
                'entrances': int(line[9]),
                'exits': int(line[10]),
                'coords': [float(line[11]), float(line[12])]
            }
            yield info


def write_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


data_gen = read_data('../data/data.txt')

DATA = {
    'info': []
}

while True:
    try:
        DATA['info'].append(next(data_gen))
    except IndexError:
        break

# DATA['info'].sort(key=lambda x: x['date'])
# print(DATA)
write_data('newdata.json', DATA)

FIRST_DAY = DATA['info'][0]['date'][3:5]
LAST_DAY = DATA['info'][-1]['date'][3:5]
DURATION = str(int(LAST_DAY) - int(FIRST_DAY))
# print(FIRST_DAY)
# print(LAST_DAY)

# print(DURATION)


