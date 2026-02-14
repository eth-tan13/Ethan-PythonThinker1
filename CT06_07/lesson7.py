# print("Hello from lesson 7")

# Recap 1

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))

# Recap 2

# total_marks = 0
# students = int(input("How many students are there?\n"))
# for i in range(int(students)):
#     marks = int(input("Enter marks:\n"))
#     total_marks = total_marks + marks
#     average_marks = total_marks / students
# print("Total = " + str(total_marks))
# print("Average = " + str(average_marks))

# Recap 3

# name = input("What is your name?\n")
# age = input("What is your age?\n")
# print(f"Hello, {name}! You are {age} years old!")

# Task 1

# for i in range(1, 11):
#     print(i)

# Task 2

# for i in range(2, 21, 2):
#     print(i)

# Task 3

# for i in range(10, 0, -1):
#     print(i)

# Task 4

# word = input("What word do you want to enter?\n")
# num = input("Repeat how many times?\n")
# for i in range(int(num)):
#     print(word)

# Task 5

# name = input("What is your name?\n")
# repeat = input("How many times do you want to repeat?\n")
# for i in range(int(repeat)):
#     print(f"Nice to meet you, {name}!")

# Task 6

# total = 0
# for i in range(5):
#     nums = input(f"What is number #{i + 1}?\n")
#     total = int(nums) + total
# print(total)

# Task 7

# num = int(input("What number for the timestable?\n"))
# for i in range(num):
#     i = int(i + 1)
#     print(f"{num} x {i} = {num * i}")

# Task 8

# num = input("Give a number\n")
# for i in range(int(num)):
#     i = i + 1
#     repeat = int(num) - (int(num) - i)
#     print(i * str(repeat))

# Task 9

# total = 0
# for i in range(5):
#     num = input(f"What is number #{i + 1}?\n")
#     total = int(num) + total
# average = total / (i + 1)
# print(average)

# Task 10

# total = 0
# students = input("How many students does your class have?\n")
# for i in range(int(students)):
#     marks = input(f"What is student #{i + 1}'s marks?\n")
#     total = int(marks) + total
# average = total / (i + 1)
# print(f"The average marks of your class is {average}")

# Task 11
# num = input("Give me a number\n")
# for i in range(int(num)):
#     i = i + 1
#     repeat = int(num) - (int(num) - i)
#     tri = "*" * repeat
#     print(tri)
# for i in range(int(num), 0, -1):
#     i = i - 1
#     repeat = int(num) - (int(num) - i)
#     tri = "*" * repeat
#     print(tri)