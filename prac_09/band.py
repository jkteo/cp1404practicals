"""Band """

class Band:
    """Band class for instances of Musician class"""

    def __init__(self, name):
        """Initialise a Band"""
        self.name = name
        self.musician = []

    def __repr__(self):
        """Represent a Band"""
        musicians = ",".join(str(musician) for musician in self.musician)
        return f"{self.name} {musicians}"

    def add(self, new_musician):
        self.musician.append(new_musician)

    def play(self):
        return '\n'.join([musician.play() for musician in self.musician])
