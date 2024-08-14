from turtle import Turtle
from bullet_class import Bullet
import random

class Alien(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.speed("fast")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.setheading(270)
        self.goto(position)
        self.direction = 5
        self.value = 10
        self.bullets = []

    def advance(self):
        self.forward(20)
        self.direction *= -1
    
    def move(self):
        self.setx(self.xcor() + self.direction)

    def shoot(self):
        if random.randint(1, 25) == 1:
            bullet = Bullet(player=False)
            bullet.goto(self.xcor(), self.ycor())
            bullet.move()
            self.bullets.append(bullet)
    
    def destroy(self):
        self.hideturtle()
        del self