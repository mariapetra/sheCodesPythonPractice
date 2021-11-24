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
player.speed(0)

# set speed variable
speed = 1

#Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed 
    speed += 1

def slow_speed():
    global speed
    speed -=1

#Set Keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(slow_speed, 'Down')
flag = True
while flag:
    player.forward(speed)





