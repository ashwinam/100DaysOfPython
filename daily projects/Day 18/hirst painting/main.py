"""
import colorgram

image_colors = colorgram.extract("image.jpg", 40)

colors_from_images = []

for color in image_colors:
    colors_from_images.append(((color.rgb.r), (color.rgb.g), (color.rgb.b)))

print(colors_from_images)
"""

from turtle import Turtle, Screen, colormode
import random

color_pallet = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
                (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
                (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
                (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
                (254, 194, 0)]


slim = Turtle()

colormode(255)

slim.speed("fastest")
slim.penup()
slim.hideturtle()

slim.setheading(225)
slim.forward(300)
slim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    slim.dot(20, random.choice(color_pallet))
    slim.forward(50)

    if dot_count % 10 == 0:
        slim.setheading(90)
        slim.forward(50)
        slim.setheading(180)
        slim.forward(500)
        slim.setheading(0)

screen = Screen()
screen.exitonclick()
