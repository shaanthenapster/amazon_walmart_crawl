from bs4 import BeautifulSoup
import urllib3
import requests

def fetch_html_data():
    links = [
        "https://www.amazon.com/dp/0142501417?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/0316428388?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/0486256936?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/0545685451?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/0634021427?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/0877793522?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/1223062341?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/1250201381?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/1250829216?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/1328910474?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/1338106449?psc=1&th=1&vs=1",
    ]

    for urls in links:
        url = 'https://api.crawlbase.com/?token=lrnHZ2r3ZkaBWJcIA_W9oQ&url=' + urls
        responses = requests.get(str(url))
        print(responses.text)

def render_data():
    with open('test2.html') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
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
    render_data()
    fetch_html_data()

