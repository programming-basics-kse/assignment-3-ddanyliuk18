import argparse

parser = argparse.ArgumentParser("Olympic Athletes")
parser.add_argument("file", help="filepath")
parser.add_argument("-medals", help="sorted medals")
parser.add_argument("country", help="code of the country")
parser.add_argument("year", help="year of olympic")
parser.add_argument("-output", help="filepath to save")
args = parser.parse_args()

with open('athlete_events.csv', newline='', encoding='utf-8') as file:
    lines = file.readlines()
    head = lines[0].strip().split(",")
    for line in lines[1:]:
        data = line.strip().split(",")