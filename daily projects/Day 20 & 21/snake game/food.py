from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        # our window is w-600 * h-600
        # so the horizontal would be -300 --------------- 300
        # vertical would be -300 ||||||||||||||||| 300
        # so food anywhere display in the window we need to set -280 280 because food 10*10
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

