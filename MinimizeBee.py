from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape

wn = Screen()

# substitute 'subsample' for 'zoom' if you want to go smaller:
smallerBee = PhotoImage(file="bee.gif").subsample(10, 10)
wn.addshape("smaller", Shape("image", smallerBee))
player = Turtle("smaller")
player.forward(100)
wn.exitonclick()



##beeimage = "bee.gif"
##wn.addshape(beeimage)
##player.shape(beeimage)
##player.penup()
##player.speed(0)
##
##smallerBee = PhotoImage(file="bee.gif").subsample(10, 10)
##wn.addshape("smaller", Shape("image", smallerBee))
##tortoise = Turtle("smaller")
##tortoise.stamp()
##screen.exitonclick()
