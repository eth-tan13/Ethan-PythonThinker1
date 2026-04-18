import time
# print("Hello from lesson 13")

# Recap 1

# acc_balance = 1000
# physical_money = 0
# print("--- ATM Machine ---")
# time.sleep(0.1)
# print("loading...")
# while True:
#     time.sleep(0.5)
#     print("Welcome to the ATM. What would you like to do today?")
#     print("1 Withdraw")
#     print("2 Deposit")
#     print("3 Check Balance")
#     print("4 Exit")
#     choice = input("Enter your choice:\n").lower()
#     time.sleep(0.25)

#     if choice == "1" or choice == "withdraw":
#         withdraw = int(input("How much money would you like to withdraw?\n"))
#         if withdraw > 1000:
#             print(f"Insufficient funds! Please try another amount less than ${acc_balance}.")
#             continue
#         else:
#             acc_balance = acc_balance - withdraw
#             physical_money = physical_money + withdraw
#             print(f"You have withdrew: {withdraw}")

#     elif choice == "2" or choice == "deposit":
#         deposit = int(input("How much money would you like to deposit?\n"))
#         if deposit < physical_money:
#             print(f"Insufficient funds! Please try another amount less than ${physical_money}.")
#             continue
#         else:
#             acc_balance = acc_balance + deposit
#             physical_money = physical_money - deposit
#             print(f"You have deposited: {deposit}")

#     elif choice == "3" or choice == "check balance":
#         print(f"Account balance: ${acc_balance}")
#         print(f"Physical money: ${physical_money}")

#     elif choice == "4" or choice == "exit":
#         break

#     else:
#         print("Invalid input! Please try again.")

# Task 1A

# fruits = ["apples", "bread", "carrots", "dates", "eggs", "flour", "grapes", "honey"]
# print(fruits)

# Task 1B

# fruits[7] = "herbs"
# print(fruits)

# Task 1C

# fruits.append("ice")
# fruits.insert(1, "bananas")
# print(fruits)

# Task 1D

# fruits.pop(1)
# print(fruits)

# Task 2

# fruits = ["apples", "bread", "carrots", "dates", "eggs", "flour", "grapes", "honey"]
# for i in range(len(fruits)):
#     if fruits[i] == "apples":
#         print(f"{fruits[i]}: I need 5 of these")
#     elif fruits[i] == "carrots":
#         print(f"{fruits[i]}: I need 3 of these")
#     elif fruits[i] == "grapes":
#         print(f"{fruits[i]}: Get the FarmFresh brand.")
#     else:
#         print(fruits[i])

# Task 3

# fruits = ["apples", "bread", "carrots", "dates", "eggs", "flour", "grapes", "honey"]
# while True:
#     added_item = input("What item have you added to your basket? (Enter end when done)\n").lower()
#     if added_item == "end":
#         break
#     else:
#         fruits.append(added_item)
# for i in range(len(fruits)):
#     print(f"I have bought: {fruits[i]}")