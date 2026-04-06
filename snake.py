from turtle import Turtle

move = 20
coordinates = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.body = []
        self.creation()

    def creation(self):
        for position in coordinates:
            self.add(position)

    def add(self,position):
            timmy = Turtle()
            timmy.color("CadetBlue2")
            timmy.shape("circle")
            timmy.penup()
            timmy.goto(position)
            self.body.append(timmy)
            self.body[0].color("CadetBlue4")

    def extend(self):
        self.add(self.body[-1].position())

    def motion(self):
        for blocks in range(len(self.body) - 1, 0, -1):
            new_x = self.body[blocks - 1].xcor()
            new_y = self.body[blocks - 1].ycor()
            self.body[blocks].goto(new_x, new_y)
        self.body[0].forward(move)

    def reset(self):
        for parts in self.body:
            parts.goto(1000,1000)
        self.body.clear()
        self.creation()
        self.body[0] = self.body[0]

    def up(self):
        if self.body[0].heading() != 270: 
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)
    
    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)