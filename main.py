import requests
from bs4 import BeautifulSoup


def get_html(url):    # фунция отсылает запрос на сервер и получ. ответ
    r = requests.get(url)   # получаю rеsponsе (ответ)
    return r.text


def main():
    url = 'https://wordpress.org/'
    print(get_html(url))






if __name__ == "__main__":    # точка входа
    main()
