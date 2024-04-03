from bs4 import BeautifulSoup

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

