from turtle import Turtle, Screen, colormode
import random

colormode(255)

chikri = Turtle()
# chikri.begin_fill()
# chikri.forward(100)
# chikri.right(90)
# chikri.forward(100)
# chikri.right(90)
# chikri.forward(100)
# chikri.right(90)
# chikri.forward(100)
# chikri.end_fill()

# Challenge 2 dashed line - - - - - - - - -

# for _ in range(30):
#     if _ % 2 == 0:
#         chikri.penup()
#         chikri.forward(10)
#     else:
#         chikri.pendown()
#         chikri.forward(10)

# Challenge 3 draw multiple shapes

colours = ["medium purple", "medium violet red", "rosy brown", "gold", "dark cyan", "sky blue", "light sea green"]


#
# def draw_shapes(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         chikri.forward(100)
#         chikri.right(angle)
#
#
# for _ in range(3, 11):
#     chikri.color(random.choice(colours))
#     draw_shapes(_)

# challenge 4 Random Walk


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]

# chikri.pensize(15)
chikri.speed("fastest")


# for _ in range(300):
#     chikri.color(random_color())
#     chikri.forward(30)
#     chikri.setheading(random.choice(directions))


########### Challenge 5 - Spirograph ########


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        chikri.color(random_color())
        chikri.circle(100)
        chikri.setheading(chikri.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
