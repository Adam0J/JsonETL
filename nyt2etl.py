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
            print(self.read_json)
        return self.read_json

    def remove_data_types(self):
        for dictionary in self.read_json:
            if dictionary == 'price':
                for x in dictionary.values():
                    if type(x) == dict:
                         = int(x.values())


        # need to return as specific data types - int, float, date

            # if dictionary == dictionary['price']:
            #     for key in dictionary:
            #         if key["$numberInt"] is int:
            #             key["$numberInt"] = int(key["$numberInt"])

            # if key is <data type> and assign
            # then remove the key

            # "price": {"$numberInt": "27"}
        return self.read_json

    def remove_bestseller_column(self):

        return self.new_columns

    def change_data_format(self):

        return self.new_columns

    def json_to_csv(self):

        return self.csv_format

    def load_csv(self):

        pass

    def main(self, json_file):
        e = Etl()
        e.extract()
        e.remove_data_types()
        pass
