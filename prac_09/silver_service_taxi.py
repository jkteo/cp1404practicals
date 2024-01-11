from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    price_per_km = 1.23

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.flagfall = 4.50

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, plus fare of ${self.flagfall:.2f} flagfall"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def drive(self, distance):
        """Drive like parent Car"""
        distance_driven = super().drive(distance)
        return distance_driven
