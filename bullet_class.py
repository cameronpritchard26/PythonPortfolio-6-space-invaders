from turtle import Turtle

class Bullet(Turtle):

    def __init__(self, player: bool):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.speed("fast")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        if player:
            self.color("white")
            self.setheading(90)
            self.goto(0, -280)
        else:
            self.color("red")
            self.setheading(270)
            self.goto(0, 280)

    def move(self):
        self.forward(20)
    
    def destroy(self):
        self.hideturtle()
        del self