import csv
import urllib.request
import urllib
import ssl
from data.get_new_file import get_last


class Info:

    def __init__(self, filename=None):
        self.filename = filename
        self.size = 0
        self.data_type = None
        self.source = filename
        if filename is None:
            self.data = None
        elif filename.endswith('txt'):
            self.data = self.txt_read(filename)
            self.data_type = 'txt'
        elif filename.endswith('csv'):
            self.data = self.csv_read(filename)
            self.data_type = 'csv'

    def get_data_type(self):
        return self.data_type

    def get_size(self):
        return self.size

    def get_source(self):
        return self.source

    def txt_read(self, filename):
        """
        (str, list) -> list
        Function read data from txt file
        """
        # limiter
        k = 0

        counter = 0
        DATA = []
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(filename, context=context) as webpage:
            webpage.readline()
            for b in webpage:
                line = b.strip()
                self.size += 1
                line = line.decode("utf-8")
                curr_st = line.split(',')[3]
                curr_el = line.split(',')[2]
                curr_date = line.split(',')[6]

                if counter > 0:
                    if curr_st == prev_st:
                        if curr_el != prev_el:
                            self.size -= 1
                            continue

                if counter > 0:
                    if curr_date == prev_date:
                        self.size -= 1
                        continue


                prev_el = curr_el
                prev_st = curr_st
                prev_date = curr_date
                counter += 1

                DATA.append(line)

                k += 1
                if k == 2000:
                    break

        return DATA


    def csv_read(self, filename):
        """
        (str) -> list

        Function reads from csv file and returns a list
        """
        DATA = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                newrow = []
                for el in row:
                    newrow.append(el.lower())
                self.size += 1
                DATA.append(newrow[3:6] + newrow[-2:])

        return DATA

    def write(self, filename):
        with open(filename, 'w') as file:
            for i in self.data:
                file.write(i + '\n')
            # file.write(self.data)
        print("data was written")


    def __add__(self, other):
        txt_data = self.data if self.filename.endswith('txt') else other.data
        csv_data = self.data if self.filename.endswith('csv') else other.data
        DATA = []
        numbers = [str(i) for i in range(10)]
        for line in txt_data:
            line = line.lower().split(",")
            for s in csv_data:
                if s[0] in line:
                    if s[2] in line:
                        line.append(str(s[-2]))
                        line.append(str(s[-1]))
                        break
                    else:
                        if [i for i in line[3] if i in numbers] \
                                == [i for i in s[2] if i in numbers] \
                                and abs(len(line[3]) - len(s[2])) <= 4:

                            line.append(str(s[-2]))
                            line.append(str(s[-1]))
                            break
                        else:
                            pass
            line = ",".join(line)
            DATA.append(line)

        newInfo = Info()
        newInfo.size = self.get_size() + other.get_size()
        newInfo.data = DATA
        newInfo.data_type = 'combined {} and {}'.format(self.get_data_type(), other.get_data_type())
        newInfo.source = "{} data + {} data".format(self.get_data_type(), other.get_data_type())
        return newInfo

    def __str__(self):
        s = "Contains {} data\nSize: {} lines\nsource: {}".format(self.get_data_type(), self.get_size(), self.get_source())
        return s


if __name__ == "__main__":
    txt_data = Info("http://web.mta.info/developers/" + get_last()[0])
    csv_data = Info("Stations.csv")
    # print(txt_data)
    # print(csv_data)
    data = txt_data + csv_data
    data.write('data.txt')
    # print(txt_
