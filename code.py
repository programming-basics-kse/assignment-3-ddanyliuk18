import argparse
import csv

class OlympicData:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.read_file()


    def read_file(self):
        all_data = []
        with open(self.filepath, "r", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i in reader:
                all_data.append(i)
        return all_data


    def filtered_data(self, country, year):
        filtered_data = []
        for i in self.data:
            if i["NOC"] == country and i["Year"] == year and i["Medal"] != "NA":
                filtered_data.append(i)
        return filtered_data




class FindMedal:
    def __init__(self, filtered_data):
        self.filtered_data = filtered_data


    def find_top_ten(self):
        top_ten = self.filtered_data[:10]
        if not top_ten:
            print("Not found")
        else:
            for i in top_ten:
                print(f"{i['Name']}, {i['Sport']}, {i['Medal']}")

    def count_medals(self):
        medals = {"Gold": 0, "Silver": 0, "Bronze": 0 }
        for i in self.filtered_data:
            if i["Medal"] in medals:
                medals[i["Medal"]] += 1

        print(f"Gold: {medals['Gold']}")
        print(f"Silver: {medals['Silver']}")
        print(f"Bronze: {medals['Bronze']}")
        return medals




parser = argparse.ArgumentParser("Olympic Athletes")
parser.add_argument("file", help="filepath")
parser.add_argument("-medals", action="store_true", help="sorted medals")
parser.add_argument("country", help="code of the country")
parser.add_argument("year", help="year of olympic")
parser.add_argument("-output", help="filepath to save")
args = parser.parse_args()

data = OlympicData(args.file)
filtered = data.filtered_data(args.country, args.year)
medal = FindMedal(filtered)
medal.find_top_ten()
if args.medals:
    medals = medal.count_medals()

