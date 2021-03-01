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
        self.timestamp = ''

    def extract(self):
        with open(self.json_file, encoding='utf-8') as file:
            for line in file:
                self.read_json.append(json.loads(line))
        return self.read_json

    def remove_data_types(self):
        return self.read_json

    def remove_bestseller_column(self):
        for i in self.read_json:
            del i["bestsellers_date"]
        self.new_columns = self.read_json
        return self.new_columns

    def change_data_format(self):
        t = [1211587200000, 1212192000000, 1212796800000]
        for book in self.new_columns:
            timesstamp = book[1]
            date = self.datetime(timestamp / le3)
        print(self.timestamp)

#your_timestamp = 1331856000000
#date = datetime.datetime.fromtimestamp(your_timestamp / 1e3)


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
