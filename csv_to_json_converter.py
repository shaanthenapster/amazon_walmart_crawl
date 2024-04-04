import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    print()
    data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print(csv_reader)
        for row in csv_reader:
            print(row)
            data.append(row)

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    csv_file_path = '/home/sanub/PycharmProjects/walmart_amazon/book_info_100.csv'
    json_file_path = '/home/sanub/PycharmProjects/walmart_amazon/az_json_dump_sample.json'
    csv_to_json(csv_file_path, json_file_path)
