"""
Estimate: 30 minutes
Actual:   40 minutes
Write a program to read this file, process the data and display processed information.
the champions and how many times they have won.
the countries of the champions in alphabetical order
The solution uses 4 functions including main.
a list of lists, a dictionary and a set.
"""
import csv


def main():
    """read wimbledon.csv and display info"""
    champions, countries = get_data("wimbledon.csv")
    print_champions(champions)
    print_winning_countries(countries)


def get_data(file):
    """interpret data from file and return info"""
    champions = {}
    countries = []
    with open(file, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header from file
        for line in reader:
            winner = line[2]
            country = line[1]
            # add names and count into champions list
            if winner in list(champions.keys()):
                champions[winner] += 1
            else:
                champions[winner] = 1
            # add unique countries into countries that won
            if country not in countries:
                countries.append(country)
    return champions, countries


def print_champions(champions):
    """Print athlete and amount of times they won"""
    print(f"Wimbledon Champions:")
    for name, win_amount in champions.items():
        print(f"{name} {win_amount}")


def print_winning_countries(countries):
    """Print countries that won"""
    countries.sort()
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(', '.join([country for country in countries]))

main()
