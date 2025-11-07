from myfunctions import*
turtle.bgcolor(64, 128, 191)
bob.speed(0)
turtle.tracer(False)

#background
bob.width(10)
for times in range(128):
     bob.color(times,160,times * 2)
     bob.circle(times * 3)
     bob.forward(times * 3)
     bob.left(91)

jump(300,230)
bob.begin_fill()
bob.color(0,128,0)
bob.circle(380)
bob.end_fill()

#flower
jump(0,0)
bob.width(6)
for times in range(128):
    bob.color(255,times * 2, times * 2)
    bob.penup()
    polygont(155,3)
    
    bob.left(81)
    bob.forward(times * 3)
    bob.pendown()

for times in range(25):
    jump(0,0)
    bob.color(255,times * 10,0)
    bob.left(times * 90 + 90)
    comet(5,5,40)
