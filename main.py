import requests
from bs4 import BeautifulSoup


def get_html(url):    # фунция отсылает запрос на сервер и получ. ответ
    r = requests.get(url)   # получаю rеsponsе (ответ)
    return r.text


def get_data(html):    # парсинг страницы
    soup = BeautifulSoup(html, 'lxml')    # преобразование хтмл в дерево объектов питона 
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text    # поиск в дереве(хтмл) по ключевым тегам
    return h1





def main():    # распечатал хтмл код страницы
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))






if __name__ == "__main__":    # точка входа
    main()
