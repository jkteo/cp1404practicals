"""
CP1404/CP5632 Practical
Kivy GUI program for dynamic labels
Started 18/12/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to for dynamic labels."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.colors = ["black", "white", "yellow", "brown"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for color in self.colors:
            new = Label(text=color)
            self.root.ids.main.add_widget(new)


DynamicLabelsApp().run()
