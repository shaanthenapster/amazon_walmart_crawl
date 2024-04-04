from bs4 import BeautifulSoup
import requests
import csv


def fetch_html_data():
    links = [
        "https://www.amazon.com/dp/B00OYJCM0O?th=1&vs=1",
        "https://www.amazon.com/dp/B000C59UIQ?psc=1&th=1&vs=1",
        "https://www.amazon.com/dp/B000C5C4QG?th=1&vs=1",
        "https://www.amazon.com/dp/B00006JPF2?th=1&vs=1",
        # "https://www.amazon.com/dp/B00BD27ZE8?th=1&vs=1",
        # "https://www.amazon.com/dp/B07BGY26VY?th=1&vs=1",
        # "https://www.amazon.com/dp/B07SNGYMXK?th=1&vs=1",
        # "https://www.amazon.com/dp/B0823B4V1Q?psc=1&th=1&vs=1",
        # "https://www.amazon.com/dp/B09BRHB2L2?psc=1&th=1&vs=1",
        # "https://www.amazon.com/dp/B09F8SK675?psc=1&th=1&vs=1",
        # 'https://www.amazon.com/dp/1632206862?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/1680450263?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B000002OU8?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00005A3L1?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B0000E2OAT?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B0001DJVFQ?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B0002RNSKK?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B0006IX7Y2?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B0009JXYNM?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B0009K9MQE?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B000BZZ3S8?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B000C9RUDY?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B000C9WLA6?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B000CGB3B2?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B000CICHMY?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B000CSS8UE?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B000EP8D7I?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B000F9O85E?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B000FJU56K?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B000MX2ORM?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B000NDZ234?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B000SDROMG?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B000YZ1R9O?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B0012P3VU8?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B001CGFQDW?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B001PYHF9E?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B001V8RYTA?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00203U69K?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B0024KMQ6K?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B0025ZPX6O?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B002C8EZV8?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B002R863WW?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B002TI7MIO?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00318NQFY?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B003549ZJA?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B003D3NEEU?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B003FHQSA6?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B003R41NB6?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B003UEBQ2E?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B004922P30?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B004I51LEW?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B004JBCE32?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B004Q9XLW0?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B004XD03RK?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B005FKMUHQ?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00605YR7G?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B0087QK1CG?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B008ND28SI?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B008VX01P2?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B0094B2G9E?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B0098JILSW?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00A7X4M1S?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00B7YLKTS?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00BAO15UE?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00CIU93TE?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00CLOG5MK?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00COKU2AW?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00DQQQNLA?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00FJ2JBR2?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00GG0RLJQ?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00GLQX3CO?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00HTI0N58?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00HU3F1WC?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00L59D9HG?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00NF1YW4G?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00OR1KPL2?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00OYJCM0O?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00PWE79S0?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00QI0IDWS?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00RYH0DGS?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00S7O6RG2?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00SLKWHXY?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00SYIJZBU?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00T3LRIJS?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00TREI0A2?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00WIQNBRI?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00X69BUSI?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B00Y1PNULG?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B00Y3L21WM?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B011MIVMSC?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B0131RG6VK?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B014BU2J6M?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B015FY4WC2?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B0163TTCL4?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B016NZK776?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B0193XJZ1Y?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B0195XJAZI?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B01ACUA8HC?psc=1&th=1&vs=1',
        # 'https://www.amazon.com/dp/B01B87TMOS?psc=1&th=1&vs=1', 'https://www.amazon.com/dp/B01BV4E68U?psc=1&th=1&vs=1'
    ]

    book_info = []

    for urls in links:
        url = 'https://api.crawlbase.com/?token=lrnHZ2r3ZkaBWJcIA_W9oQ&url=' + urls
        responses = requests.get(str(url))
        product_info = render_data(responses)
        product_info['url'] = url  # Add URL to product info
        book_info.append(product_info)
    return book_info


def render_data(values):
    soup = BeautifulSoup(values.text, 'lxml')
    book_info = {}
    # logic for iterating table data
    if soup.find('div', {'id': 'prodDetails'}):
        th = soup.find('div', {'id': 'prodDetails'}).find_all('th')
        td = soup.find('div', {'id': 'prodDetails'}).find_all('td')
        for header, value in zip(th, td):
            book_info[str(header.text).strip()] = str(value.text).replace('\n                \u200e', '').replace('\n',
                                                                                                                  '').strip()
    for div in soup.find_all('span', {'id': 'productTitle'}):
        book_description = div.text.strip()
        book_info['product_title'] = book_description
    print(book_info)
    return book_info


def write_csv(data, filename='book_info_100.csv'):
    if data:
        # Extract field names from the data
        fieldnames = set().union(*(d.keys() for d in data))
        # Add 'url' field to the fieldnames
        fieldnames.add('url')
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book_info in data:
                writer.writerow(book_info)


if __name__ == '__main__':
    write_csv(fetch_html_data())
