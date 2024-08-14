from turtle import Turtle

class Barrier(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fast")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.setheading(270)
        self.goto(position)

    def destroy(self):
        self.hideturtle()
        del self