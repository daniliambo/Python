# title Converter csv to json
# description with Class
# code

import json
import csv


class Converter:
    """
    Converter class
    """

    def __init__(self, csv_path, json_path):
        self.ipath = csv_path
        self.opath = json_path
        print('Create instance')

    def read(self):
        with open(self.ipath, 'r', newline='') as f:
            return list(csv.DictReader(f, delimiter=','))

    def write(self, content):
        content = json.dumps(content)
        with open(self.opath, 'w') as f:
            f.write(content)


def main():
    csv_path = './input.csv'
    json_path = './output.json'
    conv = Converter(csv_path=csv_path, json_path=json_path)

    content = conv.read()
    print(content)
    conv.write(content)


if __name__ == "__main__":
    print('init')
    main()
    # load_json()
    print('fin')
