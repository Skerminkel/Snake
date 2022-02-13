from Snake import Snake
from turtle import Screen
from food import Food
from settings import WIDTH, HEIGHT
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("grey")
screen.title("Snake, but worse")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.onkeypress(fun=snake.left, key="a")
screen.onkeypress(fun=snake.right, key="d")
screen.onkeypress(fun=snake.up, key="w")
screen.onkeypress(fun=snake.down, key="s")

RUNNING = True

while RUNNING:

    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.refresh_score()

    if snake.detect_collision():
        scoreboard.game_over()
        snake.reset_sake()


screen.exitonclick()
