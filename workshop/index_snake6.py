# Turtle Graphics Game - Space Turtle Chomp
import turtle
import math
import random

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
player.penup()
player.speed(0)

#create Food
maxFoods = 6
foods = []
food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(random.randint(-290, 290), random.randint(-290, 290))

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

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

#Set Keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(slow_speed, 'Down')

while True:
    player.forward(speed)

    #Boundary Player Checking a x coordiante
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(120)

    #Boundary Player Checking a y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(120)

     # Boundary Food Checking x coordinate
    if food.xcor() > 290 or food.xcor() <-290:
        food.right(130)

    # Boundary Food Checking y coordinate
    if food.ycor() > 290 or food.ycor() <-290:
        food.right(130) 
    
    # Move food around
    food.forward(3)

    # Collision checking
    if isCollision(player, food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
        food.right(random.randint(0, 360))

    

