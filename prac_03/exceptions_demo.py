"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    It will occur when the value entered is not a integer

2. When will a ZeroDivisionError occur?
    It will occur when the denominator is 0, because int cannot be divided by 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, reject any input for denominator that is not 0

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Re-enter the denominator, cannot be 0: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")