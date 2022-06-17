from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_y_cor):
        # Creating Paddle
        # width 20, height 100 xpos 350 y pos 0
        super().__init__()
        self.x_y_cor = x_y_cor
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.paddle_position(self.x_y_cor)

    def paddle_position(self, position):
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
