# # Question 1
# file = open('name.txt', 'w')
# name = input("Enter your name:")
# print(name, file=file)
# file.close()
#
# # Question 2
# file = open('name.txt', 'r')
# print(file.read())
# file.close()
#
# # Question 3
# file = open('numbers.txt', 'r')
# numbers = file.readlines()
# sum_of_numbers = int(numbers[0]) + int(numbers[1])
# print(sum_of_numbers)
# file.close()

#Question 4
file = open('numbers.txt', 'r')
numbers = file.readlines()
sum_of_numbers = 0
for lines in range(0, len(numbers)):
    sum_of_numbers += int(numbers[lines])
print(sum_of_numbers)
file.close()
