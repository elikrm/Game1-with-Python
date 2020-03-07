# Turtle Graphics Game – Space Turtle Chomp
import turtle
import math
import random
import winsound
from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape
# Set up screen
turtle.setup(700,700)
wn = turtle.Screen()
wn.bgcolor('pink')
wn.bgpic('kbgame-bg.png')
#wn.tracer(3)

# Create variable score
score = 0

# Create player turtle
player = turtle.Turtle()
#player.color('Teal')
#player.shape('turtle')
#player.penup()
#player.speed(0)

beeimage = "bee.gif"
#wn.addshape(beeimage)
#player.shape(beeimage)
smallerBee = PhotoImage(file="bee.gif").subsample(10, 10)
wn.addshape("smaller", Shape("image", smallerBee))
player = Turtle("smaller")
player.penup()
player.speed(0)

# Create opponent turtle
comp = turtle.Turtle()
comp.color('black')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Create food
maxFoods = 20
foods = []
for count in range(maxFoods):
    foods.append (turtle.Turtle())
    foods[count].shapesize(.5)
    foods[count].color("red")
    foods[count].shape("circle")
    foods[count].penup()
    foods[count].speed(0)
    foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))

# Draw the score on the screen
mypen =turtle.Turtle()
mypen.penup()
mypen.hideturtle()
mypen.setposition(-290, 310)
scorestring ="Score: %s" % score
mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
# Define functions
def turn_left():
    player.left(10)

def turn_right():
    player.right(10)

def increase_speed():
    global speed
    speed += 5
def decrease_speed():
    global speed
    speed -= 5
def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False
# Set speed variable
speed = 1

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, 'Down')
#food.setposition(-100, 100)
while True:
    #player.shapesize(.1)
    player.forward(speed)
    comp.forward(12)
    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        
    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        
    # Boundary comp Checking x coordinate
    if comp.xcor() > 290 or player.xcor() < -290:
        comp.right(random.randint(-290, 290))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        
    # Boundary comp Checking y coordinate
    if comp.ycor() > 290 or player.ycor() < -290:
        comp.right(random.randint(-290, 290))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    for food in foods:
        # Move food around
        food.forward(10)

        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180)
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
        # Collision checking
        d = math.sqrt(math.pow(player.xcor() - food.xcor(), 2) + math.pow(player.ycor() - food.ycor(),2))
        if isCollision(player, food):
        #food.hideturtle()
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
            score +=1
    # Draw the score on the screen
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-290, 310)
    scorestring ="Score: %s" % score
    mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
