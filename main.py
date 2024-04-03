from bs4 import BeautifulSoup
import requests
import csv

def fetch_html_data():
    links = [
        "https://www.amazon.com/dp/0142501417?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/0316428388?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/0486256936?psc=1&th=1&vs=1",
    ]

    for urls in links:
        url = 'https://api.crawlbase.com/?token=lrnHZ2r3ZkaBWJcIA_W9oQ&url=' + urls
        responses = requests.get(str(url))
        render_data(responses)


def render_data(values):
    soup = BeautifulSoup(values.text, 'lxml')
    book_info = {}
    for item in soup.find('div', {'id': 'detailBullets_feature_div'}).find_all('li'):
        try:
            key = item.text.split(':')[0].strip()
            value = item.text.split(':')[1].strip()
            book_info[key] = value
        except IndexError:
            print(f"Error: {item.text} does not have a value.")

    for keys, values in book_info.items():
        print(keys, values)


if __name__ == '__main__':
    fetch_html_data()
