from urllib.request import urlopen  # for Python 3: from urllib.request import urlopen
from bs4 import BeautifulSoup
from unchanged_data import URL, START_STR


def get_last():
    soup = BeautifulSoup(urlopen(URL))
    lst = []
    for link in soup.find_all('a'):
        if str(link.get('href')).startswith(START_STR):
            lst.append(link.get('href'))
            if len(lst) == 1:
                break
    return lst
