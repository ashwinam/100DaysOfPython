from turtle import Turtle, Screen
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snakey Peaky Game")
screen.tracer(0)
positions = [0, -20, -40]

turtle_lists = []

for square in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=positions[square], y=0)
    turtle_lists.append(new_turtle)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    for turtle in range(len(turtle_lists)-1, 0, -1):
        new_x = turtle_lists[turtle - 1].xcor()
        new_y = turtle_lists[turtle - 1].ycor()
        turtle_lists[turtle].goto(new_x, new_y)

    turtle_lists[0].forward(20)
    turtle_lists[0].left(90)

screen.exitonclick()
