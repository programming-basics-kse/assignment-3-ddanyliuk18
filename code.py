import argparse
parser = argparse.ArgumentParser("Olympic Athletes")
parser.add_argument("file", help="filepath")
parser.add_argument("-medals", help="sorted medals")
parser.add_argument("country", help="code of the country")
parser.add_argument("year", help="year of olympic")
parser.add_argument("-output", help="filepath to save")
args = parser.parse_args()

