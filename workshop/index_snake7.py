# Turtle Graphics Game - Space Turtle Chomp
import turtle
import math
import random

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('darkturquoise')
wn.bgpic('kbgame-bg.gif')
wn.tracer(3)

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
maxFoods = 10
foods = []

for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.color("red")
    new_food.shape("circle")
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)

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
    speed -= 1

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

    # Move food around
    for food in foods:
        food.forward(3)

        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() <-290:
            food.right(130)

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() <-290:
            food.right(130) 

        # Collision checking
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))

    

