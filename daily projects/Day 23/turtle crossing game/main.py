import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross The Road")
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.running_car()

    # detect collision with cars
    for each in car.cars:
        if player.distance(each) < 30:
            is_game_on = False

#     check the player reached the top
    if player.ycor() > 270:
        player.starting_position()
        car.speed_up()

screen.exitonclick()
