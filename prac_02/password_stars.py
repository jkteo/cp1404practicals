def main():
    display_password(get_password())


def display_password(password):
    """Print * to length of password."""
    for i in range(password):
        print("*", end="")


def get_password():
    """Handles password input and validation."""
    min_length = 2
    password = input("Please enter password:")
    len_password = len(password)
    while len_password < min_length:
        print("Invalid password length")
        password = input("Please enter password:")
        len_password = len(password)
    return len_password


main()
