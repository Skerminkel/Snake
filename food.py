from turtle import Turtle
from random import randrange
from settings import LEFT_BORDER, RIGHT_BORDER, TOP_BORDER, BOTTOM_BORDER


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("red")
        self.up()
        self.refresh()
        self.speed("fastest")

    def refresh(self):

        self.goto(x=randrange(LEFT_BORDER + 20, RIGHT_BORDER - 20, 20),
                  y=randrange(BOTTOM_BORDER + 20, TOP_BORDER - 20, 20))
        self.pos()
