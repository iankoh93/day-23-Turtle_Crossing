from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_DISTANCE = 600


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(r.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.goto(300, r.randint(-250, 260))


class CarManager:
    def __init__(self):
        self.car_List = []
        self.garageNum = 10

    def new_car(self):
        if 1 == r.randint(1, self.garageNum):
            self.car_List.append(Car())

    def move_garage(self):
        for i in range(0, len(self.car_List)):
            self.car_List[i].goto(self.car_List[i].xcor()-MOVE_INCREMENT, self.car_List[i].ycor())

    def widen_garage(self):
        if self.garageNum > 2:
            self.garageNum -= 1
