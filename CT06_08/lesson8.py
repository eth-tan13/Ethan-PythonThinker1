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

# questions = input("How many questions do you want to answer?\n")
# for i in range(int(questions)):
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     num3 = num1 * num2
#     answer = int(input(f"What is {num1} x {num2}?\n"))
#     if answer == num3:
#         print("True")
#     else:
#         print("False")

# Task 7

# num = int(input("Give me a number\n"))
# num = num % 2
# if num == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# Task 8

# num1 = int(input("Input Number #1\n"))
# num2 = int(input("input Number #2\n"))
# num3 = num1 % num2
# print(num3 == 0)

# Challenge 1

# score = 0
# total_score = 3
# user_input1 = input("What is the capital of France?\n").lower()
# print(f"Your answer: {user_input1}")
# if user_input1 == "paris":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect! The correct answer was Paris.")
# user_input2 = input("Who wrote 'To Kill A Mockingbird'?\n").lower()
# print(f"Your answer: {user_input2}")
# if user_input2 == "harper lee":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect! The correct answer was Harper Lee.")
# user_input3 = input("What is the smallest planet in our solar system?\n").lower()
# print(f"Your answer: {user_input3}")
# if user_input3 == "mercury":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect! The correct answer was Mercury.")
# print(f"Quiz completed! Your final score is {score}/{total_score}.")

# Challenge 2

import random
num1 = random.randint(1, 100)
print("Guess the number between 1 and 100. You have 5 attempts.")
for i in range(5):
    print(f"Attempt {i + 1}/5")
    guess = int(input("Guess the number:\n"))
    if guess == num1:
        print("You guessed the correct number!")
        break
    else:
        print(f"Your guess was too high: {guess > num1}")
        print(f"Your guess was too low: {guess < num1}")
print(f"Game Over. The number was: {num1}")