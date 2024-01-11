"""
CP1404/CP5632 Practical
unreliable car class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        """Initialise Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car"""
        number = random.randint(0, 100)
        if number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
