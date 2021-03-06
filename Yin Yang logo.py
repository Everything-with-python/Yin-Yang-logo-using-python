from turtle import *

def pattern(x,y):
    width(2)
    color("black",x)
    begin_fill()
    circle(150.,180)
    circle(300,180)
    left(180)
    circle(-150.,180)
    end_fill()
    left(90)
    up()
    forward(300*0.35)
    right(90)
    down()
    color(x,y)
    begin_fill()
    circle(300*0.20)
    end_fill()
    left(90)
    up()
    backward(300*0.35)
    down()
    left(90)

reset()
pattern("black","white")
pattern("white","black")
mainloop()