usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

numbers = []
for i in range(5):
    number = int(input("Enter numbers: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f" The first number is {sum(numbers) / len(numbers)}")

username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

