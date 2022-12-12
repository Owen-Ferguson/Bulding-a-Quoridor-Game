import turtle

bg = "gainsboro"
line = "black"
fill = "white"

turtle.tracer(0, 0)

def square(dim, line, fill):  
    t.color(line, fill)
    t.begin_fill()
    for i in range(4):
        t.forward(dim) # Forward turtle by s units
        t.left(90)
    t.end_fill()


def move(x, y):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()


turtle.screensize(canvwidth=400, canvheight=400,
                  bg=bg)

t = turtle.Turtle()

t.speed("fastest")
coordx = -360
coordy = 240

def row(coordx, coordy):
    for i in range(9):
            move(coordx, coordy)
            square(70, line, fill)
            coordx += 80

row(coordx, coordy)
coordx = -360
for i in range(6):
    coordy -= 80
    row(coordx, coordy)

t.hideturtle()
turtle.update()
turtle.exitonclick()