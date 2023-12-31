def main():
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {convert_celsius_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            # Convert F to C and display the result
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {convert_fahrenheit_celsius(fahrenheit):.2f} F")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_fahrenheit(celsius):
    """Converts celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_celsius(fahrenheit):
    """Convert fahrenheit celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
