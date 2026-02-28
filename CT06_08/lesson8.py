import time
import random

# print("Hello from lesson 8")

# Recap 1

# total = 1
# for i in range(5):
#     num = input(f"What is number #{i + 1}?\n")
#     total = int(num) * total
# print(f"The product of the 5 numbers are {total}")

# Task 1

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# countdown = input("Which number do you want to countdown from?\n")
# for i in range(int(countdown), 0, -1):
#     print(i)
#     time.sleep(1)

# Task 2

# num = random.randint(1, 6)
# print(num)

# for i in range(20):
#     print(random.randint(0, 9999))

# Task 3

# boolean1 = True
# boolean2 = True
# print(boolean1 == boolean2)

# Task 4

# num1 = random.randint(1, 50)
# num2 = random.randint(1, 50)
# num3 = num1 + num2
# answer = int(input(f"What is {num1} + {num2}?\n"))
# print(answer == num3)

# Task 5

# guess = input("Guess the number from 1 to 10\n")
# num1 = random.randint(1, 10)
# print(f"The number was {num1}!")
# print(guess == num1)

# Task 6

# questions = input("How many questions do you want to answer?\n")
# for i in range(int(questions)):
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     num3 = num1 * num2
#     answer = int(input(f"What is {num1} x {num2}?\n"))
#     print(answer == num3)