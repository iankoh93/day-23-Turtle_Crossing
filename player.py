from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.score = 0
        self.setheading(NORTH)
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])
        self.speed("fastest")

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def check_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION[0], STARTING_POSITION[1])
            self.score += 1
            return True
