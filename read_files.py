import csv
import urllib.request
import urllib
import ssl


def read_csv(filename):
    """
    (str) -> list

    Function reads from csv file and returns a list
    """
    lst_of_csv = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            newrow = []
            for el in row:
                newrow.append(el.lower())
            lst_of_csv.append(newrow[3:6]+newrow[-2:])

    return lst_of_csv


def read_txt(target_url, lst_of_csv):
    """
    (str, list) ->

    Function merges two data bases and writes into one
    """
    k = 0
    numbers = [str(i) for i in range(10)]
    context = ssl._create_unverified_context()
    f = open("data.txt", 'w')
    with urllib.request.urlopen(target_url, context=context) as webpage:
        webpage.readline()
        for b in webpage:
            line = b.strip()
            line = line.decode("utf-8")
            line = line.lower().split(",")
            for s in read_csv('Stations.csv'):
                if s[0] in line:
                    if s[2] in line:
                        line.append(str(s[-2]))
                        line.append(str(s[-1]))
                    else:
                        if [i for i in line[3] if i in numbers]\
                                == [i for i in s[2] if i in numbers]\
                                and abs(len(line[3]) - len(s[2])) <= 4:

                            line.append(str(s[-2]))
                            line.append(str(s[-1]))
                        else:
                            pass
            line = ",".join(line)
            f.write(line)
            f.write("\n")
            k += 1
            if k == 2000:
                break


if __name__ == "__main__":
    read_txt("http://web.mta.info/developers/data/nyct/turnstile/"
             "turnstile_190302.txt", read_csv("Stations.csv"))
