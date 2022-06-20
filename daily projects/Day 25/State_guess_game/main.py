import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
timmy = Turtle()

screen.title("guess the state")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
timmy.hideturtle()
timmy.penup()


data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_guess = screen.textinput(title=f"{len(guessed_state)}/50 Guessed.",
                                    prompt="Whats another state name?").title()
    if answer_guess == "Exit":
        missing_states = []
        for state in list_of_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_guess in list_of_states:
        guessed_state.append(answer_guess)
        state = data[data.state == answer_guess]
        timmy.goto(int(state.x), int(state.y))
        timmy.write(answer_guess)

