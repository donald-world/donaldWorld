import turtle
import random
turtle.setup(1960,1280,0,0)
turtle.penup()
turtle.fd(-750)
turtle.pendown()
turtle.pensize(10)
#turtle.pencolor("red")
turtle.colormode(255)
#turtle.seth(45)
#turtle.fd(200)
for i in range(9800,9812):
    r=random.randrange(0,255,10)
    g=random.randrange(0,255,10)
    b=random.randrange(0,255,10)
    turtle.pencolor(r,g,b)
    turtle.write(chr(i),font=(None,100))
    turtle.penup()
    turtle.fd(120)
    turtle.pendown()

turtle.done()
