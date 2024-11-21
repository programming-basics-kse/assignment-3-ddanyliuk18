import argparse

def read_file():
    with open('athlete_events.csv', "r", encoding='utf-8') as file:
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

parser = argparse.ArgumentParser("Olympic Athletes")
parser.add_argument("file", help="filepath")
parser.add_argument("-medals", help="sorted medals")
parser.add_argument("country", help="code of the country")
parser.add_argument("year", help="year of olympic")
parser.add_argument("-output", help="filepath to save")
args = parser.parse_args()

medal_counts = {"Gold" :  0, "Silver" : 0, "Bronze": 0}

print(read_file())