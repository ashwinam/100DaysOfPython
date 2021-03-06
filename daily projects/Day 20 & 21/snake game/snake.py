from turtle import Turtle

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_lists = []
        self.create_snake()
        self.head = self.turtle_lists[0]

    def create_snake(self):
        for snake in SNAKE_POSITIONS:
            self.add_snake(snake)

    def add_snake(self, snake):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(snake)
        self.turtle_lists.append(new_turtle)

    def reset(self):
        for tur in self.turtle_lists:
            tur.goto(1000, 1000)
        self.turtle_lists.clear()
        self.create_snake()
        self.head = self.turtle_lists[0]

    def extend(self):
        self.add_snake(self.turtle_lists[-1].position())

    def move(self):
        for turtle in range(len(self.turtle_lists) - 1, 0, -1):
            new_x = self.turtle_lists[turtle - 1].xcor()
            new_y = self.turtle_lists[turtle - 1].ycor()
            self.turtle_lists[turtle].goto(new_x, new_y)
        # the logic for this for loop is we just bind the coordinates for each other, if one's move
        # the first position is taken by second and seconds pos is taken by third.
        self.turtle_lists[0].forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

