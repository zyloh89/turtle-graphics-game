# Turtle Graphics Game – Space Turtle Chomp

import turtle
import math
import random
import winsound
import time

# Set up screen
turtle.setup(700,700)
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("water.gif")
wn.tracer(3)

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
player.turtlesize(2)
player.color('hotpink1')
player.shape('turtle')
player.penup() # won't leave a line when it moves, eg. penup you don't draw, pendown you do draw
player.speed(0)

# Create opponent turtle
comp = turtle.Turtle()
comp.color('red')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Create competition score
mypen2 = turtle.Turtle()
mypen2.color('red')
mypen2.hideturtle()

# Create variable score
score = 0
comp_score = 0

# Create food
#create the maximum number of cabbages and an empty list
maxFoods = 10
foods = []

# create a for loop using maxFoods
for count in range(maxFoods):
    foods.append (turtle.Turtle())
    foods[count].color("seagreen3")
    foods[count].shape("circle")
    foods[count].shapesize(.5)
    foods[count].penup()
    foods[count].speed(0)
    foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))

# Set speed variable
speed = 1

# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10*6

# Define functions
def turn_left():
        player.left(30) #turns 30degrees left, keys needs to be pushed and let go

def turn_right():
        player.right(30)

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    speed -= 1

# Collision checking using a function
def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

# Set keyboard binding
# onkey method - computer listen to a cretain key, when pressed, runs assigned function
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, 'Down')

while True:
    gametime = 0
    if gametime == 6 or time.time() > timeout:
        break
    gametime = gametime - 1

    player.forward(speed)
    comp.forward(4)

    #Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    #Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    #Boundary Comp Checking x coordinate
    if comp.xcor() > 280 or comp.xcor() <-280:
        comp.right(random.randint(30,155))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    #Boundary Comp Checking y coordinate
    if comp.ycor() > 280 or comp.ycor() <-280:
        comp.right(random.randint(30,155))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    #Move Food around
    for food in foods:
        food.forward(3)

        #Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() <-290:
           food.right(180)
           winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

        #Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() <-290:
           food.right(180)
           winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

        #Player Collision checking
        if isCollision(player, food):
           food.setposition(random.randint(-290, 290), random.randint(-290, 290))
           food.right(random.randint(0,360))
           winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
           score+=1
           #Draw the score on the screen
           mypen.undo()
           mypen.penup()
           mypen.hideturtle()
           mypen.setposition(-290, 310)
           scorestring ="Score: %s" %score
           mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

       # Comp Collision checking
        if isCollision(comp, food):
           food.setposition(random.randint(-290, 290), random.randint(-290, 290))
           food.right(random.randint(0,360))
           winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
           comp_score+=1
           #Draw the Comp score on the screen
           mypen2.undo()
           mypen2.penup()
           mypen2.hideturtle()
           mypen2.setposition(200, 310)
           scorestring ="Score: %s" %comp_score
           mypen2.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


if (int(score) > int(comp_score)):
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
    time.sleep(15)
else:
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You LOOSE", False, align="center", font=("Arial", 28, "normal"))