from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    return tim.forward(20)


def move_backward():
    return tim.backward(20)


def move_left():
    tim.setheading(tim.heading() + 10)


def move_right():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
