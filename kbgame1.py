# Turtle Graphics Game – Space Turtle Chomp

import turtle
import math
import random

# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('midnightblue')

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(2)
mypen.color('lightsteelblue')
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('hotpink1')
player.shape('turtle')
player.penup() #won't leave a line when it moves, eg. penup you don't draw, pendown you do draw
player.speed(0)

# Create food
food = turtle.Turtle()
food.color("seagreen3")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(-100, 100)
food.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Set speed variable
speed = 1

# Define functions
def turn_left():
        player.left(30) #turns 30degrees left, keys needs to be pushed and let go

def turn_right():
        player.right(30)

def increase_speed():
    global speed
    speed += 1

# Set keyboard binding
# onkey method - computer listen to a cretain key, when pressed, runs assigned function
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

while True:
    player.forward(speed)

    # Boundary Player Checking x coordinate
    if player.xcor() >290 or player.xcor() <-290:
        player.right(180)
    
    #Boundary Player Checking y coordinate
    if player.ycor() >290 or player.ycor() <-290:
        player.right(180)

    # Collision checking
    d = math.sqrt(math.pow(player.xcor() - food.xcor(), 2) + math.pow(player.ycor() - food.ycor(),2))
    if d < 20:
        food.hideturtle()

