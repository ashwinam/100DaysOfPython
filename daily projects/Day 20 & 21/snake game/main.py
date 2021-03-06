from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snakey Peaky Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.turtle_lists[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
