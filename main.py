from bs4 import BeautifulSoup
import requests

def fetch_html_data():
    links = [
        "https://www.amazon.com/dp/B00OYJCM0O?th=1&vs=1"
    ]

    for urls in links:
        url = 'https://api.crawlbase.com/?token=lrnHZ2r3ZkaBWJcIA_W9oQ&url=' + urls
        responses = requests.get(str(url))
        render_data(responses)

def render_data(values):
    soup = BeautifulSoup(values.text, 'lxml')
    book_info = {}

    # logic for iterating table data
    if soup.find('div', {'id': 'prodDetails'}):
        th = soup.find('div', {'id': 'prodDetails'}).find_all('th')
        td = soup.find('div', {'id': 'prodDetails'}).find_all('td')
        for header, value in zip(th, td):
            book_info[str(header.text).strip()] = str(value.text).replace('\n                \u200e', '').replace('\n', '').strip()
    for div in soup.find_all('span', {'id': 'productTitle'}):
        book_description = div.text.strip()
        book_info['product_title'] = book_description
    print(book_info)

    # for item in soup.find('div', {'id': 'detailBullets_feature_div'}).find_all('li'):
    #     try:
    #         key = item.text.split(':')[0].strip()
    #         value = item.text.split(':')[1].strip()
    #         book_info[key] = value
    #     except IndexError:
    #         print(f"Error: {item.text} does not have a value.")
    #


if __name__ == '__main__':
    fetch_html_data()
