"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()

    guitars.sort()

    # Loop through and display all guitars (using their str method)
    for guitar in guitars:
        print(guitar)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitars.append(Guitar(name, year, cost))  # add to list of guitars
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    with open("guitars.csv", "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            print(guitar)
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print(f"{len(guitars)} guitars saved to guitars.csv")


main()
