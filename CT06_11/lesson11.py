# print("Hello from lesson 11")

# Recap 1

# px = int(input("Give me the price of the item that you are buying!\n"))
# if px <= 5:
#     print("Sounds good!")
# elif px <= 50:
#     print("Are you sure you need this?")
# elif px <= 500:
#     print("Where are you getting this money from?!")
# else:
#     print("Don't even think about it!")

# Task 1

# rider1 = int(125)
# rider2 = int(150)
# if rider1 > 120 and rider2 > 120:
#     print("You are eligible to ride!")
# else:
#     print("You are not eligible to ride!")

# Task 2

# num = int(input("Input a number!\n"))
# if num % 7 == 0 and num % 3 == 0:
#     print(f"{num} is divisible by 3 and 7!")
# else:
#     print(f"{num} is not divisible by 3 and 7!")

# Task 3

# first_name = input("What is your first name?\n").lower()
# last_name = input("What is your last name?\n").lower()
# if first_name == "james" and last_name == "leong":
#     print("YOU ARE WANTED.")
# else:
#     print("Have a nice day :3")

# Task 4

# rider1 = int(input("Enter your age!\n"))
# rider2 = int(input("Enter your age!\n"))
# if rider1 >= 18 or rider2 >= 18:
#     print("You are allowed to ride!")
# else:
#     print("You are not allowed to ride!")

# Task 5

# age = int(input("Enter your age!\n"))
# if age < 12 or age > 65:
#     print("Ticket price: $15")
# else:
#     print("Ticket price: $20")

# Task 6

# gender = input("Enter your gender:\n").lower()
# if gender == "m" or gender == "male":
#     print("Valid input")
# else:
#     print("Invalid input")

# Task 7

# while True:
#     green = input("Enter the correct colour:\n").lower()
#     if not green == "green":
#         print("Incorrect colour! Try again.")
#     else:
#         print("Correct! The colour is green!")
#         break

# Task 8

# day = input("What day is it today?\n").lower()
# if not day == "saturday":
#     print("It's not the weekend yet!")
# else:
#     print("The weekend has arrived. Happy weekend!")


# Task 9

# while True:
#     password = input("Enter your password:\n")
#     if not password == "Python123":
#         print("Access Denied.")
#     else:
#         print("Correct password. Access Granted.")
#         break

# Task 10

# print("What do you want to eat?")
# burger = input("A burger? (Yes/No)\n").lower()
# drink = input("A drink? (Yes/No)\n").lower()
# fries = input("Some fries? (Yes/No)\n").lower()
# if burger == "yes" and fries == "yes" and drink == "no":
#     print("Won't you get thirsty?")
# elif burger == "no" and fries == "no" and drink == "no":
#     print("GET OUT OF THE RESTAURANT. NOW.")
# else:
#     print("Ok, order registered!")

# Task 11

# username = "John123"
# password = "pw123"
# username_input = input("Enter your username:\n")
# password_input = input("Enter your password:\n")
# if username_input == username and password_input == password:
#     print("Access Granted")
# elif username_input == username or password_input == password:
#     print("Username or password is incorrect.")
# else:
#     print("Access Denied.")

# Task 12

game_status = "active"
if game_status == "active":
    print("Game in progress...")
    
