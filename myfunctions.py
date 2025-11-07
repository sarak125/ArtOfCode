import turtle
from random import*
bob = turtle.Turtle()
turtle.colormode(255)

def square(size):
    for times in range(4):
        bob.forward(size)
        bob.left(90)

def triangle(size):
    for times in range(3):
        bob.forward(size)
        bob.left(120)

def pentagon(size):
    for times in range(5):
        bob.forward(size)
        bob.left(72)

def polygont(size, side):
    angle = 360/side
    bob.begin_fill()
    for times in range(side):
        bob.forward(size)
        bob.left(angle)
    bob.end_fill()

def polygon(size, side,C):
    angle = 360/side
    bob.color(C)
    bob.begin_fill()
    for times in range(side):
        bob.forward(size)
        bob.left(angle)
    bob.end_fill()

def comet(size, angle, length):
    for times in range(length):
        bob.forward(size)
        bob.left(angle)
        bob.width(times)

def jump(x,y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()

def stair(distance, amount, C, W):
    bob.color(C)
    bob.width(W)
    for times in range(amount):
        bob.forward(distance)
        bob.left(90)
        bob.forward(distance)
        bob.right(90)

def drawSquare(size, radius):
    for times in range(6):
        bob.forward(size)
        bob.right(90)
        bob.circle(radius)

def drawTriangle(size, radius):
    for times in range(6):
        bob.forward(size)
        bob.right(120)
        bob.circle(radius)

def tree(x, y):
    jump(x, y)
    polygon(100, 3, "green")
    bob.forward(37)
    bob.right(90)
    polygon(25, 4, "brown")
    bob.left(90)

def flower(c):
    bob.right(90)
    bob.right(120)
    polygon(30, 5, c)
    for times in range(4):
        bob.forward(35)
        bob.right(72)
        polygon(30, 5, c)
    bob.color("yellow")
    bob.begin_fill()
    bob.right(123)
    bob.forward(12)
    bob.circle(29)
    bob.end_fill()
    bob.left(180)
    bob.left(60)

def star(size, c):
    for times in range(5):
        bob.color(c)
        bob.forward(size)
        bob.left(144)

def starborder():
    jump(-460,315)
    for times in range(6):
        r = randint(0, 255)
        g = randint(0, 255)
        c = (r,g,0)
            
        bob.begin_fill()
        star(c)
        bob.penup()
        bob.forward(150)
        bob.pendown()
        bob.end_fill()

    jump(-460,-340)
    for times in range(6):
        r = randint(0, 255)
        b = randint(0, 255)
        c = (r,0,b)
            
        bob.begin_fill()
        star(c)
        bob.penup()
        bob.forward(150)
        bob.pendown()
        bob.end_fill()

def spiral(size,w,c):
    bob.width(w)
    bob.color(c)
    for times in range(size):
        bob.forward(times)
        bob.left(35)
        
    
