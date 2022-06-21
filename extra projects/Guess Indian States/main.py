import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=800)
image = "india_blank_map_img.gif"
screen.addshape(image)
turtle.shape(image)

# indian_map = {
#     "states": ["Jammu and Kashmir", "Himachal Pradesh", "Punjab", "Uttarakhand", "Haryana", "Delhi", "Rajasthan",
#                "Uttar Pradesh", "Bihar", "Gujarat", "Madhya Pradesh", "Jharkhand", "West Bengal",
#                "Maharashtra", "Chhattisgarh", "Odisha", "Telangana", "Goa", "Karnataka", "Andhra Pradesh",
#                "Kerala", "Tamil Nadu", "Sikkim", "Arunachal Pradesh", "Meghalaya", "Assam", "Nagaland",
#                "Tripura", "Manipur", "Mizoram"],
#     "x": [-167.0, -130.0, -173.0, -80.0, -159.0, -131.0, -232.0, -58.0, 80.0, -260.0, -107.0, 66.0, 132.0, -167.0,
#           -36.0, 41.0, -90.0, -210.0, -173.0, -83.0, -152.0, -102.0, 152.0, 309.0, 229.0, 267.0, 300.0, 232.0, 284.0,
#           261.0],
#     "y": [321.0, 247.0, 213.0, 196.0, 165.0, 148.0, 98.0, 109.0, 65.0, -6.0, -2.0, 20.0, -10.0, -91.0, -75.0, -74.0,
#           -133.0, -208.0, -222.0, -222.0, -337.0, -327.0, 119.0, 144.0, 64.0, 84.0, 76.0, 16.0, 38.0, 3.0]
# }
#
# ind_map = pandas.DataFrame(indian_map)
# ind_map.to_csv("indian_map.csv")

# return the screen clicked coordinates
# def get_the_coor(x,y):
#     print(f"the clicked coordinates is {x}, {y}")
#
#
# turtle.onscreenclick(get_the_coor)
#
# turtle.mainloop()


# TODO : get the states name and there coordinates [done]
# TODO : put the question mark on map
# TODO : check the answer guess with our csv file:
# if it correct then put there state name on there coordinate.


data = pandas.read_csv("indian_map.csv")
all_states = data.states.to_list()
print(all_states)

# TODO : check the answer_guess in all_states:
#     if it correct then put it into the map

guessed_state = []

while len(guessed_state) < 30:
    answer_guess = turtle.textinput(title="Guess the state", prompt="Whats you guess?").title()
    if answer_guess in all_states:
        guessed_state.append(answer_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.states == answer_guess]  # get the state row
        t.goto(int(state.x), int(state.y))
        t.write(answer_guess)

screen.exitonclick()
