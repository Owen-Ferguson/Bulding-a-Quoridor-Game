"""QuoridorX module

Implements the graphic mode of a Quoridor game (automatic or manual)
"""

import turtle
from quoridor import Quoridor

class QuoridorX(Quoridor):
    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs)   

        #Setting colour names for quick reference
        self.bg = "gainsboro"
        self.line = "black"
        self.fill = "white"
        self.p1_col = "red"
        self.p2_col = "blue"

        #Set screensize and instance for the turtle
        # turtle.screensize(canvwidth=400, canvheight=400, bg=self.bg)
        self.t = turtle.Turtle()

        #Lists are used to erase previous move before moving the player
        self.p1_movelist = []
        self.p2_movelist = []

        #Hand-picked coords for the top left corner
        self.coordx = -325
        self.coordy = 250

    #Create a filled square
    def square(self):
        #Renders the whole board instantly rather than watching the turtle go
        turtle.tracer(0, 0)

        self.t.color(self.line, self.fill)
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(66)
            self.t.left(90)
        self.t.end_fill()

    #Move to any spot on the board without making marks
    def move(self, x, y):
        self.t.penup()
        self.t.setx(x)
        self.t.sety(y)
        self.t.pendown()
        # turtle.exitonclick()

    #Create a full row of squares for the empty board
    def row(self):
        for i in range(9):
                self.move(self.coordx, self.coordy)
                self.square()
                self.coordx += 70

    #Add player 1 or 2 to the board
    def place_player(self, x, y, player):
        self.coordx = -325
        self.coordy = 250


        #Remove the player from previous position
        if player == 1:
            if len(self.p1_movelist) > 0:
                self.remove_player(self.p1_movelist[-1][0], self.p1_movelist[-1][1])
        if player == 2:
            if len(self.p2_movelist) > 0:
                self.remove_player(self.p2_movelist[-1][0], self.p2_movelist[-1][1])
        
        #Add the player to the new location
        self.move(self.coordx + 70*(x - 1) + 33, (self.coordy + 70*(y - 9) + 8))
        if player == 1:
            self.t.color(self.line, self.p1_col)
            self.p1_movelist.append((x, y))
        elif player == 2:
            self.t.color(self.line, self.p2_col)
            self.p2_movelist.append((x, y))
        self.t.begin_fill()
        self.t.circle(25)
        self.t.end_fill()
    
    #Remove the player from the previous position; to be called when moving a player
    def remove_player(self, x, y):
        self.move(self.coordx + 70*(x - 1) + 33, (self.coordy + 70*(y - 9) + 8))
        self.t.color(self.fill, self.fill)
        #Drawing over the old position with the same colour as the board
        self.t.begin_fill()
        self.t.circle(25)
        self.t.end_fill()

    #Create a filled rectangle for the walls
    def wall(self, x, y, orientation):
        #Change the wall dimensions + coords based on orientation
        if orientation == "MH":
            self.move(self.coordx + 70*(x - 1) + 3, self.coordy + 70*(y - 9) - 9)
            self.length = 129
            self.width = 15
        elif orientation == "MV":
            self.move(self.coordx + 70*(x - 1) - 10, self.coordy + 70*(y - 9) + 3)
            self.length = 15
            self.width = 129

        #Place a black rectangle at the given coords
        self.t.color(self.line)
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(self.length)
            self.t.left(90)
            self.t.forward(self.width)
            self.t.left(90)
        self.t.end_fill()

    def create_empty_board(self):
        turtle.tracer(0, 0)
        self.row()
        for i in range(8):
            self.coordx = -325
            self.coordy -= 70
            self.row()
        self.t.hideturtle()

    def gui(self):
        state = self.état
        
        self.create_empty_board()
        for i in range(2):
            self.place_player(state["joueurs"][i]["pos"][0]\
                , state["joueurs"][i]["pos"][1], i + 1)
        
        if len(state["murs"]["horizontaux"]) > 0:
            for i in state["murs"]["horizontaux"]:
                self.wall(i[0], i[1], "MH")

        if len(state["murs"]["verticaux"]) > 0:
            for i in state["murs"]["verticaux"]:
                self.wall(i[0], i[1], "MV")

        # turtle.update()
        # turtle.exitonclick()
