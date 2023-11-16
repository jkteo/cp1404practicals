def main():
    menu = """
    (G)et a valid score (must be 0 - 100 inclusive)
    (P)rint result
    (S)how stars
    (Q)uit"""
    print(menu)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":  # get valid score
            pass
        if choice == "P":  # print result
            pass
        if choice == "S":  # show stars
            pass
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
    pass


main()
