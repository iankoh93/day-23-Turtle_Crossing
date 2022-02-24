from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write("Score: 0", move=False, font=FONT)

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", move=False, font=FONT)
