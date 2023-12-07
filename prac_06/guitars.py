"""
Program that uses the Guitar class
"""
from prac_06.guitar import Guitar


def main():
    """takes in new guitars and prints guitar objects"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name} ({year} : ${cost} added.)")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitars, 1):
        is_vintage = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}:{guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {is_vintage}")


main()
