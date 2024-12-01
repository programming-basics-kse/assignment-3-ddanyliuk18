import argparse
from olympicdata import OlympicData
from country import Country
from medalfind import FindMedal
from optional import output_to_file


parser = argparse.ArgumentParser("Olympic Athletes")
parser.add_argument("file", help="filepath")
parser.add_argument("-medals", nargs=2, metavar = ("country", "year"), help="sorted medals")
parser.add_argument("-overall", nargs = "+",
                    help="overall the best amount of medals for country ", dest="countries")
parser.add_argument("-total", help="data of all countries")
parser.add_argument("-interactive", action="store_true", help="enter data fir yourself")
parser.add_argument("-o", "--output", help="filepath to save")

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
        output_to_file(args.output, f"Medals in {year} for {country}: {medals}")


if args.total:
    year = args.total
    country_medals = data.medals_by_year(year)
    for i in country_medals.items():
        print(f"{i[0]} - Gold: {i[1]['Gold']}, Silver: {i[1]['Silver']}, Bronze: {i[1]['Bronze']}")

if args.countries:
     best_years = data.medal_by_country(args.countries)
     for country, (year, medals) in best_years.items():
         if year is not None:
             print(f"{country} best result was {medals} medals in Olympics {year}")
         else:
             print(f"Unfortunately no medals found for {country}")



if args.interactive:
    main_country = input("Please, enter your country: ")
    data_for_country = Country(main_country, data.data)
    data_for_country.first_appeared()
    data_for_country.find_max()
    data_for_country.find_min()
    data_for_country.find_average()


