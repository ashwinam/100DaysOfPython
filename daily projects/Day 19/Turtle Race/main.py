from turtle import Turtle, Screen
import random
screen = Screen()

is_game_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="bet", prompt="What is your bet? Enter the color: ")
colors = ["red", "green", "blue", "orange", "purple", "yellow"]
all_turtles = []
turtle_positions = [-100, -60, -20, 20, 60, 100]

for _ in range(0, 6):
    sally = Turtle(shape="turtle")
    sally.color(colors[_])
    sally.penup()
    sally.goto(x=-230, y=turtle_positions[_])
    all_turtles.append(sally)

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You Won! the winner is {winning_color}.")
            else:
                print(f"You Lose! the winner is {winning_color}.")
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)

# # molly
# molly = Turtle(shape="turtle")
# molly.color(colors[1])
# molly.penup()
# molly.goto(x=-230, y=-60)
#
# # dolly
# dolly = Turtle(shape="turtle")
# dolly.color(colors[2])
# dolly.penup()
# dolly.goto(x=-230, y=-20)
#
# # polly
# polly = Turtle(shape="turtle")
# polly.color(colors[3])
# polly.penup()
# polly.goto(x=-230, y=20)
#
# # golly
# golly = Turtle(shape="turtle")
# golly.color(colors[4])
# golly.penup()
# golly.goto(x=-230, y=60)
#
# # folly
# folly = Turtle(shape="turtle")
# folly.color(colors[5])
# folly.penup()
# folly.goto(x=-230, y=100)


screen.exitonclick()
