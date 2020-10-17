import requests
from bs4 import BeautifulSoup


def get_html(url1):    # фунция отсылает запрос на сервер и получ. ответ
    r = requests.get(url1)   # получаю rеsponsе (ответ)
    return r.text


def get_data(html):    # парсинг страницы
    soup = BeautifulSoup(html, 'lxml')    # преобразование хтмл в дерево объектов питона 
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text    # поиск в дереве(хтмл) по ключевым тегам
    return h1





def main():    # собирает результат работы др.функций
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))






if __name__ == "__main__":    # точка входа
    main()
