# Turtle Graphics Game - Space Turtle Chomp
import turtle

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('darkturquoise')

# Create player turtle
player = turtle.Turtle()
player.color('magenta')
player.shape('turtle')
player.pendown()

# set speed variable
speed = 1

while True:
    player.forward(speed)