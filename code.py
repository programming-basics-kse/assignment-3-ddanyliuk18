import argparse

def read_file(filepath):
    with open(filepath, "r", encoding='utf-8') as file:
        lines = file.readlines()
        head = lines[0].strip().split(",")
        all_data = []
        for line in lines[1:]:
            data = line.strip().split(",")
            rows = {}
            for i in range(len(head)):
                rows[head[i]] = data[i]
            all_data.append(rows)
    return all_data


def filtered_data(data, country, year):
    filtered_data = []
    for i in data:
        if i["NOC"] == country and i["Year"] == year:
            filtered_data.append(i)
    return filtered_data



parser = argparse.ArgumentParser("Olympic Athletes")
parser.add_argument("file", help="filepath")
parser.add_argument("-medals", help="sorted medals")
parser.add_argument("country", help="code of the country")
parser.add_argument("year", help="year of olympic")
parser.add_argument("-output", help="filepath to save")
args = parser.parse_args()

data = read_file(args.file)
country = args.country
year = args.year

filtered = filtered_data(data, country, year)

if filtered:
    print(f"Filtered data for {country} in {year}:")
    for i in filtered:
        print(i)
else:
    print(f"No data found for {country} in {year}.")

