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

screen.exitonclick()