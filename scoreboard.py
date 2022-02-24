from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write("Score: 0", move=False, font=FONT)

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", move=False, font=FONT)

    def game_over(self, score):
        self.clear()
        self.goto(0, 0)
        self.write(f"Your final score: {score}", move=False, font=FONT, align="center")
