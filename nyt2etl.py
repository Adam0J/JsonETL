import csv
import json
from datetime import datetime


class Etl:
    def __init__(self):
        self.json_file = ""
        self.new_csv_file = ''
        self.read_json = []
        self.new_columns = ''
        self.csv_format = [[]]
        self.datetime = ''

    def extract(self):
        with open(self.json_file, encoding='utf-8') as file:
            for line in file:
                self.read_json.append(json.loads(line))
        return self.read_json

    def remove_data_types(self):
        keys = list(self.read_json[0].keys())
        for dictionary in self.read_json:
            for key in keys:
                values = dictionary[key]
                if isinstance(values, dict):
                    values = list(values.values())[0]
                    if isinstance(values, dict):
                        values = list(values.values())[0]
                        dictionary[key] = values
                    else:
                        dictionary[key] = values

        return self.read_json

# if dictionary == dictionary['price']:
#     value = int(value)

    def transform_data(self):
        for dictionary in self.read_json:
            for key in dictionary:
                if key == 'price':
                    dictionary[key] = float(dictionary[key])
                elif key == 'rank' or key == 'rank_last_week' or key == 'weeks_on_list' or key == 'published_date':
                    dictionary[key] = int(dictionary[key])
        return self.read_json

    def remove_bestseller_column(self):

        for i in self.read_json:
            del i["bestsellers_date"]
        self.new_columns = self.read_json
        return self.new_columns

    def change_data_format(self):
        # Iterate through self.new_columns with parameter book
        for book in self.new_columns:
            old_format = int(book['published_date'])
            # Convert old date format into YYYY-mm-DD format
            date = datetime.fromtimestamp(old_format / 1e3)
            date = date.strftime("%Y-%m-%d")
            # Return date into book
            book['published_date'] = date
        return self.new_columns

    def json_to_csv(self):
        for x in self.read_json[0].keys():
            self.csv_format[0].append(x)

        for dictionary in self.read_json:
            self.csv_format.append(list(dictionary.values()))
        return self.csv_format

    def load_csv(self):
        with open(self.new_csv_file, "w",newline="", encoding='utf-8') as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(self.csv_format)

    def main(self, old_file_name, new_csv_file_name):
        self.json_file = old_file_name
        self.new_csv_file = new_csv_file_name
        self.extract()
        self.remove_data_types()
        self.transform_data()
        self.remove_bestseller_column()
        self.change_data_format()
        self.json_to_csv()
        self.load_csv()


instance = Etl()
instance.main('nyt2.json', 'new_csv_file.csv')


