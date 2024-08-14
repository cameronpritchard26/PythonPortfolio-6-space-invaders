from turtle import Turtle
from bullet_class import Bullet

class Player(Turtle):
    
        lives = 3

        def __init__(self):
            super().__init__()
            self.shape("triangle")
            self.penup()
            self.speed("fast")
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.color("white")
            self.setheading(90)
            self.goto(0, -280)
            self.bullets = []
    
        def move_left(self):
            self.setx(self.xcor() - 20)
            if self.xcor() < -280:
                self.setx(-280)
    
        def move_right(self):
            self.setx(self.xcor() + 20)
            if self.xcor() > 280:
                self.setx(280)
    
        def shoot(self):
            bullet = Bullet(player=True)
            bullet.goto(self.xcor(), self.ycor())
            bullet.move()
            self.bullets.append(bullet)
        
        def destroy(self):
            self.hideturtle()
            del self