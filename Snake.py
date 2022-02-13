from turtle import Turtle
from settings import LEFT_BORDER, RIGHT_BORDER, TOP_BORDER, BOTTOM_BORDER
START_X = 0
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:

    def __init__(self):
        self.body = []
        self.create(True)
        self.head = self.body[0]

    def create(self, arg):
        """
        :param arg: If False, will not create new body for this instance
        """

        x = START_X
        if arg:
            for _ in range(3):
                body = Turtle("square")
                body.color("white")
                body.up()
                body.goto(x, 0)
                x -= 20
                self.body.append(body)

    def move(self):
        head_pos = self.body[0].pos()
        self.body[-1].goto(head_pos)
        tail = self.body.pop()
        self.body.insert(1, tail)
        self.body[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def grow(self):

        body = Turtle("square")
        body.color("white")
        body.up()
        body.goto(self.body[-1].pos())
        self.body.append(body)

    def detect_collision(self):

        for segment in self.body[1:]:
            if self.head.pos() == segment.pos():
                return True

        if self.head.xcor() < LEFT_BORDER + 2 or self.head.xcor() > RIGHT_BORDER - 10:
            return True
        if self.head.ycor() < BOTTOM_BORDER + 10 or self.head.ycor() > TOP_BORDER:
            return True

        else:
            return False

    def reset_sake(self):
        for part in self.body:
            part.goto(RIGHT_BORDER + 100, 0)

        self.body.clear()
        self.create(True)
        self.head = self.body[0]
