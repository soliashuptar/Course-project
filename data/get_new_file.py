from urllib.request import urlopen  # for Python 3: from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_last():
    URL = 'http://web.mta.info/developers/turnstile.html'
    soup = BeautifulSoup(urlopen(URL))
    lst = []
    for link in soup.find_all('a'):
        if str(link.get('href')).startswith('data/nyct/turnstile/turnstile_'):
            lst.append(link.get('href'))
            if len(lst) == 1:
                break
    return lst
