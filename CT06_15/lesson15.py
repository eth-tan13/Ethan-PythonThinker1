import turtle
# print("Hello from lesson 15")

window = turtle.Screen()
t = turtle.Turtle()


t.seth(0)
t.pendown()
t.speed(0)
t.color("#000000")

# Normal

# Square
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# Triangle
# for i in range(3):
#     t.forward(100)
#     t.left(120)

# Pentagon
# for i in range(5):
#     t.forward(100)
#     t.left(72)

# Hexagon
# for i in range(6):
#     t.forward(100)
#     t.left(60)

# Circle
# for i in range(360):
#     t.forward(3)
#     t.left(1)

# Nested Loop

# Square
# for j in range(36):
#     for i in range(4):
#         t.forward(100)
#         t.right(90)
#     t.right(10)

# Triangle
# for j in range(36):
#     for i in range(3):
#         t.forward(100)
#         t.left(120)
#     t.right(10)

# Pentagon
# for j in range(36):
#     for i in range(5):
#         t.forward(100)
#         t.left(72)
#     t.right(10)

# Hexagon
# for j in range(36):
#     for i in range(6):
#         t.forward(100)
#         t.left(60)
#         t.right(10)

# Circle
# for j in range(36):
#     for i in range(360):
#         t.forward(3)
#         t.left(1)
#     t.right(10)

# Star
# for i in range(36):
#     for i in range(5):
#         t.forward(100)
#         t.left(144)
#     t.right(10)

# Rainbow Spirals
colours = ["#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#4B0082", "#EE82EE"]
length = 3

for i in range(100):
    for colour in colours:
        t.color(colour)
        t.forward(length)
        t.right(91) # Square = 91, Star = 145, Hexagon = 61
        length += 1


turtle.done()