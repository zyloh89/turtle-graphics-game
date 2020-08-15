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

# Set speed variable
speed = 1


while True:
    player.forward(speed)
