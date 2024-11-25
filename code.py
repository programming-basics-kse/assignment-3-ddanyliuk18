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


    def medals_by_year(self, year):
        medals_by_year = {}
        for i in self.data:
            if i["Year"] == year and i["Medal"] != "NA":
                country = i["NOC"]
                medal = i["Medal"]
                if country in medals_by_year:
                    medals_by_year[country][medal] += 1
                else:
                    medals_by_year[country] = {"Gold": 0, "Silver": 0, "Bronze": 0}
        return medals_by_year


    def filtered_data(self, country, year):
        filtered_data = []
        for i in self.data:
            if i["NOC"] == country and i["Year"] == year and i["Medal"] != "NA":
                filtered_data.append(i)
        return filtered_data


    def country_inf(self, country):
        averages = {}
        success = {}
        filtered_data = []
        years = []
        sums = []
        max_value = 0
        for i in self.data:
            if i["NOC"] == country:
                filtered_data.append(i)

        for j in filtered_data:
            medal = j["Medal"]
            year = int(j["Year"])
            place = j["City"]
            years.append(year)
            min_year = min(years)
            if year not in success:
                success[year] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            if medal != "NA":
                success[year][medal] += 1

        for year, counts in success.items():
            total = counts["Gold"] + counts["Silver"] + counts["Bronze"]
            sums.append(total)
            if total > max_value:
                max_value = total
                max_year = year

            if total < max_year:
                min_value = total
                min_year = year

            if total > 0:
                averages[year] = {
                    "Gold": counts["Gold"] / total,
                    "Silver": counts["Silver"] / total,
                    "Bronze": counts["Bronze"] / total,
                }

        print(f"\nFirst olympic was {min_year} in {place}\n")
        print(f"The max medals was {max_value} in {max_year}\n")
        print(f"The min medals was {min_value} in {min_year}\n")
        print(f"Average medal values per Olympiad: ")
        for year, avg_counts in averages.items():
            print(f"{year}: Gold: {avg_counts['Gold']:.2f}, Silver: {avg_counts['Silver']:.2f}, Bronze: {avg_counts['Bronze']:.2f}")


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
parser.add_argument("-medals", nargs=2, metavar = ("country", "year"), help="sorted medals")
parser.add_argument("-total", help="data of all countries")
parser.add_argument("-interactive", action="store_true", help="enter data fir yourself")
parser.add_argument("-output", help="filepath to save")
args = parser.parse_args()

data = OlympicData(args.file)

if args.medals:
    country = args.medals[0]
    year = args.medals[1]
    filtered = data.filtered_data(country, year)
    medal = FindMedal(filtered)
    medal.find_top_ten()
    if filtered:
        medals = medal.count_medals()


if args.total:
    year = args.total
    country_medals = data.medals_by_year(year)
    for i in country_medals.items():
        print(f"{i[0]} - Gold: {i[1]['Gold']}, Silver: {i[1]['Silver']}, Bronze: {i[1]['Bronze']}")

if args.interactive:
    main_country = input("Please, enter your country: ")
    data.country_inf(main_country)
