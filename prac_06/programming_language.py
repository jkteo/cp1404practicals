"""CP1404/CP5632 Practical - Programming language class."""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise programming language object"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return info about programming language object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns boolean based on if dynamic or not"""
        if self.typing == "Dynamic":
            return True
