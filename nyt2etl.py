import csv, json


class Etl:
    def __init__(self):
        self.json_file = "nyt2.json"
        self.new_csv_file = 'nyt2.csv'
        self.read_json = []
        self.new_columns = ''
        self.csv_format = [[]]

    def extract(self):
        with open(self.json_file, "r", encoding='utf-8') as file:
            for line in file:
                self.read_json.append(json.loads(line))
            #print(self.read_json)
        return self.read_json

    def remove_data_types(self):
        keys = list(self.read_json[0].keys())
        #print(keys)
        for dictionary in self.read_json:
            for key in keys:
                values = dictionary[key]
                if isinstance(values,dict):
                    values = list(values.values())[0]
                    if isinstance(values,dict):
                        values = list(values.values())[0]
                        dictionary[key] = values
                    else:
                        dictionary[key] = values
        return self.read_json

    def transform_data(self):
        for dictionary in self.read_json:
            for key in dictionary:
                if key == 'price':
                    dictionary[key] = round(float(dictionary[key]),2)
                elif key == 'rank' or key == 'rank_last_week' or key == 'weeks_on_list' or key == 'published_date':
                    dictionary[key] = int(dictionary[key])
        return self.read_json

    def remove_bestseller_column(self):

        return self.new_columns

    def change_data_format(self):

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

    def main(self):

        pass

test = Etl()
test.extract()
test.remove_data_types()
test.transform_data()
test.json_to_csv()
test.load_csv()