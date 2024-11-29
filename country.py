class Country:
    def __init__(self, country, data):
        self.country = country
        self.data = []
        for i in data:
            if i["NOC"] == country:
                self.data.append(i)
        self.success = self.find_success()
        self.total = self.find_total()
        self.sums = self.find_sums()
        self.max_year = self.find_max()


    def find_success(self):
        success = {}
        for i in self.data:
            year = int(i["Year"])
            medal = i["Medal"]
            if year not in success:
                success[year] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            if medal != "NA":
                success[year][medal] += 1
        return success


    def first_appeared(self):
        years = []
        for j in self.data:
            year = int(j["Year"])
            place = j["City"]
            years.append(year)
            min_year = min(years)
        print(f"\nFirst olympic was {min_year} in {place}\n")


    def value_of_year(self):
        for j in self.data:
            year = int(j["Year"])
        return year


    def find_total(self):
        total_by_year = {}
        for year, counts in self.success.items():
            total_by_year[year] = counts["Gold"] + counts["Silver"] + counts["Bronze"]
        return total_by_year

    def find_sums(self):
        sums = []
        sums.append(self.total)
        return sums


    def find_max(self):
        max_value = 0
        for year, total in self.total.items():
            if total > max_value:
                max_value = total
                max_year = year
        print(f"The max medals was {max_value} in {max_year}\n")
        return max_year


    def find_min(self):
        min_value = self.max_year
        for year, total in self.total.items():
            if total < min_value:
                min_value = total
                min_year = year
        print(f"The min medals was {min_value} in {min_year}\n")
        return min_year


    def find_average(self):
        averages = {}
        for year, counts in self.success.items():
            total = self.total[year]
            if total > 0:
                averages[year] = {
                    "Gold": counts["Gold"] / total,
                    "Silver": counts["Silver"] / total,
                    "Bronze": counts["Bronze"] / total,
            }
        for year, avg_counts in averages.items():
            print(f"{year}: Gold: {avg_counts['Gold']:.2f}, Silver: {avg_counts['Silver']:.2f}, Bronze: {avg_counts['Bronze']:.2f}")

