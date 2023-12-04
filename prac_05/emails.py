"""
emails
Estimate: 30 minutes
Actual:   40 minutes
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to extract a name from the email as in the example below.
"""


def main():
    """checks name and store in dictionary"""
    users = {}
    email = input("Email: ")
    while email != "":
        name = split_email(email)
        wrong_name = input(f"is your name {name}? (y/n): ")
        if wrong_name.upper() == "N":
            correct_name = input("Name: ")
            users[email] = correct_name
        else:
            users[email] = name
        email = input("Email: ")

    for email, name in users.items():
        print(f"{name} ({email})")


def split_email(email):
    """Obtain name from email"""
    name = email.split("@")[0]
    name = name.split(".")
    name = " ".join(name).title()
    return name


main()
