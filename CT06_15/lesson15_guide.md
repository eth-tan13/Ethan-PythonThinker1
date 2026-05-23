# Lesson 15 - Introduction to Turtle Library

## Task 1: Creating a window​
### 1a​
By importing the ‘turtle’ library and using the following functions, create ablank window that stays:​
- turtle.Screen()​
- .mainloop()​

### 1b​
Modify your code to create a window that is 600 in width and 400 in height​

Hint:​ ???.setup(width=???, height=???)​

## Task 2: Creating a Turtle​
By modifying the code you have done previously, create the following agents:​

Note: Your new code must be between the turtle.screen() and .mainloop()
function.​

### 2a​
Create an orange turtle​

1. Using ‘import’, import the ‘turtle’ library​

2. Using the ‘turtle.Turtle()’ function, create an agent called “turtle”​

3. Using the ‘.shape()’ function, set the shape of the “turtle” agent to a turtle​

4. Using the ‘.fillcolor()’ function, turn “turtle” orange.​

### 2b
Create a turtle object as a green square​

1. Using ‘import’, import the ‘turtle’ library​

2. Using the ‘turtle.Turtle()’ function, create an agent called “square”​

3. Using the ‘.shape()’ function, set the shape of the “turtle” agent to a square​

4. Using the ‘.fillcolor()’ function, turn “turtle” green.

## Task 3: Drawing​
Given the number of sides and each interior angle, draw each of the following shapes using a loop and a selection of the following functions:​

1. .seth()​
2. .up()​
3. .down()​
4. .forward()​
5. .backward()​
6. .left()​
7. .right()​

### 3a
Draw a line​
Number of sides: 1​
Interior angle: NA​

### 3b
Draw a triangle​
Number of sides: 3​
Interior angle: 120

### 3c
Draw a square​
Number of sides: 4​
Interior angle: 90

### 3d
Draw a pentagon​
Number of sides: 5​
Interior angle: 72

### 3e
Draw a hexagon​
Number of sides: 6​
Interior angle: 60

### 3f
Draw a circle​
Number of sides: 360​
Interior angle: 1

## Task 4: Creating a Crosshair​
Write a program that moves the turtle to draw a horizontal line across the middle of the screen and then a vertical line down the centre of the screen, creating a crosshair pattern.​

1. Import the ‘turtle’ library​

2. Using ‘turtle.Screen()’, create a turtle screen and set the window size to 600x400.​
Hint: ???.setup(width=???, height=???)​

3. Create a turtle, and use ‘.penup()’ to lift the pen​

4. Use ‘.goto()’ to position your turtle at x = -300 and y = 0​

5. Use ‘.pendown()’ and use ‘.setx()’ to set your turtle’s x position to x =300​

6. ‘.penup()’ and using ‘.goto()’, reposition your turtle to x = 0 and y =200​

7. Use ‘.pendown()’ and ‘.sety()’ to set your turtle’s y position to y = -200​

8. End off with a ‘.mainloop()’ function to keep your window open​

## Task 5: Random Points​
Write a program where the turtle moves to 10 random positions on the screen, drawing a small square at each spot. Display the x and y coordinates of each position next to the squares.​

1. Import ‘turtle’ and ‘random’ library​

2. Create a 600x600 turtle screen using ‘turtle.Screen()’ and ‘.setup(width=,height=)’ function​

3. Within a ‘for’ loop,​

    1. Create ‘x’ variable and assign a random value between -280 and 280.​

    2. Create a ‘y’ variable and assign a random value between -280 and 280.​

    3. Using ‘.goto()’, position your turtle at the random coordinate ‘x’ and ‘y’ generated.​

    4. Using a ‘for’ loop and the movement commands, draw a 5x5 small square​

    5. Reposition your turtle object 40 steps lower than the randomly generated x and y coordinate​

    6. Write the coordinate of the square using ‘.write()’​

## Task 6: Follow the Edge
Using ‘.xcor()’ and ‘.ycor()’ to detect the edge, make the turtle move along the perimeter of the screen, turning at the corners.​

1. Import the ‘turtle’ library​

2. Create a 400x400 screen using ‘.Screen()’ and ‘.setup’​

3. Create 2 variables that holds the x and y limit​

4. Using ‘.goto()’, position the turtle at the lower left corner of the limit​

5. Within a forever loop, use the following format for each direction, turn the turtle at each corner of the 4 corners:​
- While ‘x’ coordinate of turtle is less than ‘x’ limit,​
- Move forward​
- Turn left 90​