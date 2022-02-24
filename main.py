import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

speed = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player1 = Player()
garage = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(speed)

    garage.new_car()
    garage.move_garage()

    for car in garage.car_List:
        if car.distance(player1) < 20:
            game_is_on = False

    screen.onkeypress(fun=player1.move_up, key="Up")
    scoreboard.update_score(player1.score)

    if player1.check_finish():
        speed *= 0.9
        if player1.score % 1 == 0:
            garage.widen_garage()

    screen.update()

print("Game Over")
scoreboard.game_over(player1.score)
screen.exitonclick()
