# Turtle Graphics Game – Space Turtle Chomp

import turtle

# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')

# Create player turtle
player = turtle.Turtle()
player.color('thistle')
player.shape('turtle')
player.penup() #won't leave a line when it moves, eg. penup you don't draw, pendown you do draw
player.speed(0)

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