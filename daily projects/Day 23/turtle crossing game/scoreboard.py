from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_level()

    def update_level(self):
        self.write(arg=f"Level {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level:{self.level}", move=True, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", move=True, align="center", font=FONT)





