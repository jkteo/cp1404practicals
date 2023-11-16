def main():
    menu = """
    (G)et a valid score (must be 0 - 100 inclusive)
    (P)rint result
    (S)how stars
    (Q)uit"""
    print(menu)
    choice = input("> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":  # get valid score
            score = validate_score()
        elif choice == "P":  # print result
            print(score_result(score))
        elif choice == "S":  # show stars
            print(display_star(score))
        else:
            print("Invalid choice")
        menu = """
        (G)et a valid score (must be 0 - 100 inclusive)
        (P)rint result
        (S)how stars
        (Q)uit"""
        print(menu)
        choice = input("> ").upper()
    print("Farewell")


def validate_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def score_result(score):
    if score >= 90:
        result = "Excellent"
    elif score > 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


def display_star(score):
    for i in range(score):
        return score * "*"


main()
