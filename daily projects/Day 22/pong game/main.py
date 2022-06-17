import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Ping Pong.")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect wall collision
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Detect paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect the r_paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    # detect the l_paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()


screen.exitonclick()
