import csv, json
from datetime import datetime

class Etl:
    def __init__(self):
        self.json_file = ''
        self.new_csv_file = ''
        self.read_json = []
        self.new_columns = ''
        self.csv_format = [[]]
        self.datetime = ''

    def extract(self):
            with open(self.json_file, encoding='utf-8') as file:
                for line in file:
                    self.read_json.append(json.loads(line))
                #print(self.read_json)
            return self.read_json

    def remove_data_types(self):

        return self.read_json

    def remove_bestseller_column(self):
        for i in self.read_json:
            del i["bestsellers_date"]
        self.new_columns = self.read_json
        return self.new_columns

    def change_data_format(self):
        t = [1212883200000, 1214092800000, 1214697600000]
        for book in t:
            #timestamp = book[1]
            date = datetime.fromtimestamp(book / 1e3)
            print(date)
        return self.new_columns

    def json_to_csv(self):

        return self.csv_format

    def load_csv(self):

        pass

    def main(self, old_file_name):
        self.json_file = old_file_name
        self.extract()
        self.remove_bestseller_column()
        self.change_data_format()
        pass

instance = Etl()
instance.main('nyt2.json')