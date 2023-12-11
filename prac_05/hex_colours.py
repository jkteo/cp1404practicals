"""
CP1404/CP5632 Practical
Colours in a dictionary
"""

COLOURS = {"BLOND": "#faf0be", "BRASS": "#b5a642", "BUFF": "#f0dc82", "CAMEL": "#c19a6b", "CARDINAL": "#c41e3a",
           "CARMINE": "#960018", "CERISE": "#de3163", "CHARCOAL": "#36454f", "Citron": "#9fa91f", "CORN": "#fbec5d"}


hex_code = input("Enter colour name: ").upper()
while hex_code != "":
    try:
        print(hex_code, "is", COLOURS[hex_code])
    except KeyError:
        print("Invalid color name")
    hex_code = input("Enter colour name: ").upper()
