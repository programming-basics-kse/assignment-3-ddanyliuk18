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

    def overall_status(self, countries):
        results = {}
        for country in countries:
            countries_data = []
            for item in self.filtered_data:
                if item["NOC"] == country and item["Medal"] != "NA":
                    countries_data.append(item)
            medals_per_year = {}
            for item in countries_data:
                year = item["Year"]
                medal = item["Medal"]
                if year not in medals_per_year:
                     medals_per_year[year] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                if medal in medals_per_year[year]:
                    medals_per_year[medal] += 1

            best_years = {}
            for medal_type in ["Gold", "Silver", "Bronze"]:
                max_year = None
                max_count = 0
                for year, counts in medals_per_year.items():
                    if counts[medal_type] > max_count:
                        max_year = year
                        max_count = counts[medal_type]
                    if max_year is not None:
                        best_years[medal_type] = (max_year, max_count)
                    else:
                        best_years[medal_type] = None
            results[country] = best_years

        for country, best_years in results.items():
            print(f"The best results for {country}:")
            for medal_type, (year, count) in best_years.items():
                print(f"{medal_type}: {year} year - {count} medals")







parser = argparse.ArgumentParser("Olympic Athletes")
parser.add_argument("file", help="filepath")
parser.add_argument("-medals", action="store_true", help="sorted medals")
parser.add_argument("country",nargs = "?", help="code of the country")
parser.add_argument("year",nargs = "?", help="year of olympic")
parser.add_argument("-overall", nargs = "+", help="overall analysis of medals count")
parser.add_argument("-output", help="filepath to save")
args = parser.parse_args()

data = OlympicData(args.file)
filtered = data.filtered_data(args.country, args.year)
medal = FindMedal(filtered)
medal.find_top_ten()
if args.medals:
    medals = medal.count_medals()
if args.overall:
    medal.overall_status(args.overall)
