import csv, json


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

        return self.read_json

    def remove_bestseller_column(self):

        for i in self.read_json:
            del i["bestsellers_date"]
        self.new_columns = self.read_json
        return self.new_columns

    def change_data_format(self):

        return self.new_columns

    def json_to_csv(self):

        return self.csv_format

    def load_csv(self):

        pass

    def main(self, old_file_name):

        self.json_file = old_file_name
        self.extract()
        print(self.remove_bestseller_column())
        pass


instance = Etl()
instance.main('nyt2.json')
