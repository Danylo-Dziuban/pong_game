from turtle import Screen
import time
from player import Player
from scoreboard import ScoreBoard
from ball import Ball
from separator import Separator

screen = Screen()
screen.title('Pong')
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.tracer(0)

x_1 = -100
x_2 = 100
y = 250

# mode('logo')
player_1 = Player(-350)
player_2 = Player(350)
scoreboard_1 = ScoreBoard((x_1, y), "PLAYER 1")
scoreboard_2 = ScoreBoard((x_2, y), "PLAYER 2")
ball = Ball()
separator = Separator()

screen.onkeypress(key='w', fun=player_1.go_up)
screen.onkeypress(key='s', fun=player_1.go_down)

screen.onkeypress(key='Up', fun=player_2.go_up)
screen.onkeypress(key='Down', fun=player_2.go_down)

screen.update()
screen.listen()

game_is_on = True


while game_is_on:
    ball.move()

    if ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.bounce_off_player()

    elif ball.distance(player_2) < 50 and ball.xcor() > 320:
        ball.bounce_off_player()

    elif ball.ycor() > 280:
        ball.bounce()

    elif ball.ycor() < -280:
        ball.bounce()

    elif ball.xcor() < -380:
        scoreboard_2.update_score()
        ball.teleport(0, 0)

    elif ball.xcor() > 390:
        scoreboard_1.update_score()
        ball.teleport(0, 0)

    if scoreboard_1.score == 10:
        scoreboard_1.game_over()
        game_is_on = False
    elif scoreboard_2.score == 10:
        scoreboard_2.game_over()
        game_is_on = False

    screen.update()
    time.sleep(0.05)


screen.exitonclick()
