from turtle import Turtle
from settings import TOP_BORDER
from highscore import highscore

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = highscore
        self.score = 0
        self.hideturtle()
        self.up()
        self.goto(0, TOP_BORDER - 40)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align="center",
                   font=("Arial", 20, "normal"))

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.display_score()

    def set_high_score(self):
        with open("highscore.py", "w") as hscore:
            hscore.write(f"highscore = {self.high_score}")
