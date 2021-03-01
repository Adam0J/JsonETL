import csv
import json


class Etl:
    def __init__(self):
        self.json_file = ''
        self.new_csv_file = ''
        self.read_json = []
        self.new_columns = ''
        self.csv_format = [[]]

    def extract(self):
        with open(self.json_file, encoding='utf-8') as file:
            for line in file:
                self.read_json.append(json.loads(line))
        return self.read_json

    def remove_data_types(self):
        keys = list(self.read_json[0].keys())
        print(keys)
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

        # need to return as specific data types - int, float, date

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

        return self.new_columns

    def json_to_csv(self):
        for x in self.read_json[0].keys():
            self.csv_format[0].append(x)

        for dictionary in self.read_json:
            self.csv_format.append(list(dictionary.values))
        return self.csv_format

    def load_csv(self):

        pass

    def main(self, old_file_name):
        self.json_file = old_file_name
        self.extract()
        self.remove_data_types()
        self.remove_bestseller_column()

        pass


instance = Etl()
instance.main('nyt2.json')
