password = input("Please enter password:")
len_password = len(password)
min_length = 2

while len_password < min_length:
    print("Invalid password length")
    password = input("Please enter password:")
    len_password = len(password)
for i in range(len(password)):
    print("*", end="")
