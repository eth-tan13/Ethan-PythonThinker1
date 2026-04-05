# print("Hello from lesson 12")

# Recap 1

# num = int(input("Give me a number!\n"))
# if num % 3 == 0 and num % 5 == 0:
#     print("The number is divisible by 3 and 5!")
# else:
#     print("The number is not divisible by 3 and 5.")

# Task 1A

# import time
# visitors = 0
# while visitors < 50:
#     visitors = visitors + 1
#     time.sleep(0.25)
#     print(f"Visitors present: {visitors}")

# Task 1B

# import time
# visitors = 18
# print(f"Visitors already present: {visitors}")
# print("Max visitors allowed: 30")
# while visitors < 30:
#     visitors = visitors + 1
#     time.sleep(0.25)
#     print(f"Visitors already present: {visitors}")
#     print("Max visitors allowed: 30")

# Task 1C

# import time
# visitors = 4
# print(f"Visitors already present: {visitors}")
# print("Max visitors allowed: 30")
# while visitors < 25:
#     visitors = visitors + 1
#     time.sleep(0.25)
#     print(f"Visitors already present: {visitors}")
#     print("Max visitors allowed: 25")

# Task 2

# import time
# visitors = 0
# while visitors < 50:
#     if visitors == 30:
#         break
#     else:
#         visitors = visitors + 1
#         time.sleep(0.25)
#         print(f"Visitors present: {visitors}")

# Task 3

# order = ""
# order_add = ""
# while order_add != "end":
#     order_add = input("I'm here to take your order! What would you like? (Enter end when done)\n").lower()
#     if order_add == "end":
#         break
#     elif order == "":
#         order = order + order_add
#     else:
#         order = order + ", " + order_add
# print(f"Your order: {order}")
# print("Order has been taken! Please wait for your food!")

# Task 4A

# import time
# num = 10
# while num >= 1:
#     time.sleep(0.25)
#     print(num)
#     num -= 1
# else:
#     print("Happy New Year!")

# Task 4B

# import time
# num = 10
# while num >= 1:
#     time.sleep(0.25)
#     print(num)
#     if num == 5:
#         break
#     num -= 1
# else:
#     print("Happy New Year!")