import random


def main():
    score = float(input("Enter score: "))
    print(score_result(score))
    print(score_result(random.randint(0, 100)))


def score_result(score):
    """Returns the result based on the score."""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score > 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


main()
