from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
game_is_on = True

screen.listen()
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.teleport()
        snake.grow_snake()

    # Detect collision with walls
    elif abs(snake.head.xcor()) >= 300 \
            or abs(snake.head.ycor()) >= 300:
        game_is_on = False
        ScoreBoard.game_over()

    elif snake.crash_with_body():
        game_is_on = False
        ScoreBoard.game_over()








screen.exitonclick()

