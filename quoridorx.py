import turtle

#Setting colour names for quick reference
bg = "gainsboro"
line = "black"
fill = "white"
p1_col = "red"
p2_col = "blue"

#Renders the whole board instantly rather than watching the turtle go
turtle.tracer(0, 0)

#Create a filled square
def square(dim, line, fill):  
    t.color(line, fill)
    t.begin_fill()
    for i in range(4):
        t.forward(dim)
        t.left(90)
    t.end_fill()

#Move to any spot on the board without making marks
def move(x, y):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

#Create a full row of squares for the empty board
def row(coordx, coordy):
    for i in range(9):
            move(coordx, coordy)
            square(66, line, fill)
            coordx += 70

#Add player 1 or 2 to the board
def place_player(x, y, player):
    #Remove the player from previous position
    if player == 1:
        if len(p1_movelist) > 0:
            remove_player(p1_movelist[-1][0], p1_movelist[-1][1])
    if player == 2:
        if len(p2_movelist) > 0:
            remove_player(p2_movelist[-1][0], p2_movelist[-1][1])
    
    #Add the player to the new location
    move(coordx + 70*(x - 1) + 33, (coordy + 70*(y - 1) + 8))
    if player == 1:
        t.color(line, p1_col)
        p1_movelist.append((x, y))
    elif player == 2:
        t.color(line, p2_col)
        p2_movelist.append((x, y))
    t.begin_fill()
    t.circle(25)
    t.end_fill()

#Remove the player from the previous position; to be called when moving a player
def remove_player(x, y):
    move(coordx + 70*(x - 1) + 33, (coordy + 70*(y - 1) + 8))
    t.color(fill, fill)
    #Drawing over the old position with the same colour as the board
    t.begin_fill()
    t.circle(25)
    t.end_fill()

#Create a filled rectangle for the walls
def wall(x, y, orientation):
    #Change the wall dimensions + coords based on orientation
    if orientation == "MH":
        move(coordx + 70*(x - 1) + 3, coordy + 70*(y - 1) - 9)
        length = 129
        width = 15
    elif orientation == "MV":
        move(coordx + 70*(x - 1) - 10, coordy + 70*(y - 1) + 3)
        length = 15
        width = 129

    #Place a black rectangle at the given coords
    t.color(line)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()

#Set screensize and instance for the turtle
turtle.screensize(canvwidth=400, canvheight=400, bg=bg)
t = turtle.Turtle()

#Lists are used to erase previous move before moving the player
p1_movelist = []
p2_movelist = []

#Hand-picked coords for the top left corner
coordx = -325
coordy = 250

#Create a row on the board 9 times; gives the whole empty board
row(coordx, coordy)
for i in range(8):
    coordy -= 70
    row(coordx, coordy)

#Placing players; player# determines colour
place_player(5, 1, 1)
place_player(5, 9, 2)

#Walls can either be vertical or horizontal; the vertical alignment is 
#very very slightly off though
wall(5, 6, "MH")


#Cleaning up at the end so we don't get weird artifacts
t.hideturtle()
turtle.update()
turtle.exitonclick()