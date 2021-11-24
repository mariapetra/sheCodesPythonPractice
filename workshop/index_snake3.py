# Turtle Graphics Game - Space Turtle Chomp
import turtle

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('darkturquoise')

# Draw Border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(10)
mypen.color("yellow")
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('magenta')
player.shape('turtle')
player.pendown()
player.speed(0)

#create Food

food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()
food.speed(0)

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
while True:
    player.forward(speed)

    #Boundary Player Checking a x coordiante
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(120)

    #Boundary Player Checking a y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(120)





