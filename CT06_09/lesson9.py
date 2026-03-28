import random

# print("Hello from lesson 9")

# Recap 1

# num1 = random.randint(1,6)
# num2 = random.randint(1,6)
# num3 = random.randint(1,6)
# print(f"1st number:{num1}")
# print(f"2st number:{num2}")
# print(f"3st number:{num3}")
# random1 = num1 % 2
# random2 = num2 % 2
# random3 = num3 % 2
# if random1 % 2 == 0 and random2 % 2 == 0 and random3 % 2 == 0:
#     print("All numbers are even")
# elif random1 % 2 == 1 and random2 % 2 == 1 and random3 % 2 == 1:
#     print("All numbers are odd")
# else:
#     print("The numbers are not all even/odd")

# Task 2

# num_days = int(input("How many days has the book been borrowed?\n"))
# if num_days > 25:
#     print("Remember to return your book!")
# else:
#     print("Good boy")

# Task 3B

# num_apples = int(input("How many apples do you want to buy?\n"))
# if num_apples > 10:
#     print("You will get a 10% discount for buying that many apples!")
#     price = num_apples * 1 * 0.9
# else:
#     price = num_apples * 1
# print(f"The price of your apples is: ${round(price, 2)}")

# Task 4B

num_apples = int(input("How many apples do you want to buy?"))
num_oranges = int(input("How many oranges do you want to buy?"))
if num_apples > 5:
    print("You will get a 10% discount for buying that many apples!")
    price_apples = num_apples * 0.6 * 0.9
else:
    price_apples = num_apples * 0.6
if num_oranges > 5:
    print("You will get a 10% discount for buying that many oranges!")
    price_oranges = num_oranges * 0.9 * 0.9
else:
    price_oranges = num_oranges * 0.9
total_price = price_apples + price_oranges
print(f"The total price is: ${round(total_price, 2)}")

