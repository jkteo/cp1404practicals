"""CP1404/CP5632 Practical - Programming language class."""


class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """prints info about guitar"""
        return f"{self.name} ({self.year} : ${self.cost})"

    def __lt__(self, other):
        """sorts Guitars by year"""
        return self.year < other.year

    def get_age(self):
        """gets age of guitar"""
        return 2023 - self.year

    def is_vintage(self):
        """if age is older than 50 years, return true"""
        return self.get_age() > 50
