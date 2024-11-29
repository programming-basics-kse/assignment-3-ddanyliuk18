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

    def medal_by_country(self, countries):
        country_medals = {}
        for country in countries:
            country_medals[country] = {}
        for i in self.data:
            country = i["NOC"]
            year = i["Year"]

            if country in countries and i["Medal"] != "NA":
                if year not in country_medals[country]:
                    country_medals[country][year] = 0
                country_medals[country][year] += 1

        best_years = {}
        for country in country_medals:
            best_year = None
            max_medals = 0
            for year, medals in country_medals[country].items():
                if medals > max_medals:
                    best_year = year
                    max_medals = medals
            best_years[country] = (best_year, max_medals)
        return best_years

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

