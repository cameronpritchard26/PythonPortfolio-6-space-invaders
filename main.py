from turtle import Screen
from player_class import Player
from alien_classes import Alien
from scoreboard_class import Scoreboard
import time

game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

def generate_enemies():
    row_1 = [Alien((i * 60 - 240, 250)) for i in range(8)]
    row_2 = [Alien((i * 60 - 240, 200)) for i in range(8)]
    row_3 = [Alien((i * 60 - 240, 150)) for i in range(8)]
    return [row_1, row_2, row_3]

enemies = generate_enemies()
bottom_row = enemies[-1]

def configure_player():
    screen.listen()
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")
    screen.onkey(player.shoot, "space")

configure_player()
while game_on:
    screen.update()
    time.sleep(0.1)

    if len(enemies) == 0:
        enemies = generate_enemies()
    
    for row in enemies:
        if len(row) > 0:
            for alien in row:
                alien.move()
                if alien in bottom_row:
                    alien.shoot()
            if row[0].xcor() < -280 or row[-1].xcor() > 280:
                for alien in row:
                    alien.advance()
        else:
            enemies.remove(row)
        if len(bottom_row) == 0:
            enemies.remove(bottom_row)
            bottom_row = enemies[-1]

    # Animate the bullets
    for bullet in player.bullets:
        bullet.move()
 
    for row in enemies:
        for alien in row:
            for bullet in alien.bullets:
                bullet.move()
    
    # Check for collisions
    for p_bullet in player.bullets:
        for row in enemies:
            for alien in row:
                if p_bullet.distance(alien) < 20:
                    for a_bullet in alien.bullets:
                        a_bullet.destroy()
                    row.remove(alien)
                    alien.destroy()
                    player.bullets.remove(p_bullet)
                    p_bullet.destroy()
                    scoreboard.increase_score(alien.value)
    
    for row in enemies:
        for alien in row:
            for a_bullet in alien.bullets:
                if a_bullet.distance(player) < 20:
                    for p_bullet in player.bullets:
                        p_bullet.destroy()
                    player.destroy()
                    alien.bullets.remove(a_bullet)
                    a_bullet.destroy()
                    scoreboard.decrease_lives()
                    player = Player()
                    configure_player()

    # Check if the player has lost
    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()