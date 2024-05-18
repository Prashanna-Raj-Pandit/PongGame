from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=1200, height=900)
screen.bgcolor("black")
screen.title("Pong Game")

player1_score = ScoreBoard("one", -220, 360)
player2_score = ScoreBoard("two", 220, 360)

screen.tracer(0)

l_paddle = Paddle(560, 0, stretch_len=1)
r_paddle = Paddle(-560, 0, stretch_len=1)

for y_co in range(-540, 540, 150):
    boarder_line = Paddle(0, y_co, stretch_len=0.5)

ball = Ball()

screen.listen()

screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_over = False

while not game_over:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    if ball.ycor() > 370 or ball.ycor() < -360:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() > 520 or ball.distance(r_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 560:
        player1_score.increase_score("one")
        ball.initial_position()

    if ball.xcor() < -560:
        player2_score.increase_score("two")
        ball.initial_position()

screen.exitonclick()
