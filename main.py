import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_for,"Up")
screen.onkey(player.move_back, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # creating and moving cars for every loop
    car_manager.create_car()
    car_manager.move_cars()

    # Detecting collision and printing game over
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing, increasing up the speed of cars and increasing level
    if player.crossed_the_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.score_a_point()


screen.exitonclick()

