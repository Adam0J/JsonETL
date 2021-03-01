import csv, json
from datetime import datetime


class Etl:
    def __init__(self):
        self.json_file = ''
        self.new_csv_file = ''
        self.read_json = []
        self.new_columns = []
        self.csv_format = [[]]

    def extract(self):
        self.read_json = [json.loads(line) for line in open(self.json_file, "r", encoding="utf-8")]

    def remove_data_types(self):
        keys = list(self.read_json[0].keys())
        for i in range(len(self.read_json)):
            for key in keys:
                dict_values = self.read_json[i][key]
                if isinstance(dict_values,dict):
                    nested_values = list(dict_values.values())[0]
                    if isinstance(nested_values,dict):
                        double_nested_values = list(nested_values.values())[0]
                        self.read_json[i][key] = double_nested_values
                    else:
                        self.read_json[i][key] = nested_values
        return self.read_json

    def change_int_to_int(self):
        for i in range(len(self.read_json)):
            self.read_json[i]['price'] = float(self.read_json[i]['price'])
            self.read_json[i]['rank'] = int(self.read_json[i]['rank'])
            self.read_json[i]['rank_last_week'] = int(self.read_json[i]['rank_last_week'])
            self.read_json[i]['weeks_on_list'] = int(self.read_json[i]['weeks_on_list'])

    def remove_bestseller_column(self):
        self.new_columns = self.read_json
        for book in self.new_columns:
            del book['bestsellers_date']

    def change_data_format(self):
        for book in self.new_columns:
            old_format = int(book['published_date'])
            date = str(datetime.fromtimestamp(old_format / 1e3))
            book['published_date'] = date
        return self.new_columns

    def json_to_csv(self):
        self.csv_format = [list(self.new_columns[0].keys())]
        [self.csv_format.append(list(row.values())) for row in self.new_columns]
        # Non pythonic way
        # self.csv_format.append(list(row.values()))
        # self.csv_format.append(list(row.values()))
        # for row in self.new_columns:
        #     self.csv_format.append(list(row.values()))
        # print(self.csv_format)
        # return self.csv_format

    def load_csv(self):
        with open(self.new_csv_file, 'w', newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.csv_format)

    def main(self,json_file,new_csv_file):
        self.json_file = json_file
        self.new_csv_file = new_csv_file
        self.extract()
        self.remove_data_types()
        self.change_int_to_int()
        self.remove_bestseller_column()
        self.change_data_format()
        self.json_to_csv()
        self.load_csv()


Example = Etl()
Example.main('nyt2.json', 'newNYT2.csv')
