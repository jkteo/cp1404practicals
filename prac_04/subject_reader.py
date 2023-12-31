"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    input_file = get_data()
    data = print_data(input_file)
    print_details(data)


def get_data():
    input_file = open(FILENAME, "r")
    data = input_file.readlines()
    input_file.close()
    return data


def print_data(input_file):
    """Read data from file formatted like: subject,lecturer,number of students."""
    part = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        part.append(parts)
    return part


def print_details(parts):
    """Read data from parts formatted: CP1401 is taught by Ada Lovelace and has 192 students"""
    for line in parts:
        print(f"{line[0]} is taught by {line[1]} and has {line[2]} students")


main()
