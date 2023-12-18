"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Started 18/12/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.609


class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles to km """
    number = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        """Calculate miles to km"""
        miles = float(value)
        self.handle_update(miles)

    def increment_input(self, delta):
        """Increase or decrease the input"""
        current_value = int(self.root.ids.input_number.text)
        new_value = current_value + int(delta)
        self.root.ids.input_number.text = str(new_value)

    def handle_update(self, value):
        """Update by pressing enter"""
        self.number = str(float(value) * MILES_TO_KM)


ConvertMilesApp().run()
