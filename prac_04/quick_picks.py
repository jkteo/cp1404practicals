import random

LENGTH = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    lines = int(input("How many quick picks? "))
    while lines < 0:
        print("Invalid amount, try again")
        lines = int(input("How many quick picks? "))

    for i in range(lines):
        data = []
        generate_random(data)
        print(" ".join(f"{number:2}" for number in data))


def generate_random(data):
    """generate random number in list with no duplicates"""
    for i in range(LENGTH):
        random_no = random.randint(MIN_NUMBER, MAX_NUMBER)
        while random_no in data:
            random_no = random.randint(MIN_NUMBER, MAX_NUMBER)
        data.append(random_no)
    return data.sort()


main()
