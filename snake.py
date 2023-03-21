from turtle import Turtle
import random

TURTLE_SIZE = 20
TURTLE_PACE = 20


def _new_box(previous_turtle=None, head=None):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.shapesize(1, 1, 1)
    turtle.penup()
    if previous_turtle is not None:
        if head is None or head.heading() == 0:
            turtle.goto(previous_turtle.xcor() - TURTLE_SIZE, previous_turtle.ycor())
        elif head.heading() == 90:
            turtle.goto(previous_turtle.xcor(), previous_turtle.ycor() - TURTLE_SIZE)
        elif head.heading() == 180:
            turtle.goto(previous_turtle.xcor() + TURTLE_SIZE, previous_turtle.ycor())
        elif head.heading() == 270:
            turtle.goto(previous_turtle.xcor(), previous_turtle.ycor() + TURTLE_SIZE)
    return turtle


class Snake(Turtle):
    """Holds and controls the snake object"""

    def __init__(self):
        super().__init__()
        self.game_is_on = True
        self.turtles = []
        for index in range(3):
            previous_turtle = self.turtles[index - 1] if index > 0 else None
            self.turtles.append(_new_box(previous_turtle))

        self.head = self.turtles[0]

        for turtle in self.turtles:
            print(f"Turtle added at {turtle.xcor()} and {turtle.ycor()}")

    def move(self):
        for index in range(len(self.turtles) - 1, 0, -1):
            turtle_ahead_x = self.turtles[index - 1].xcor()
            turtle_ahead_y = self.turtles[index - 1].ycor()
            self.turtles[index].setx(turtle_ahead_x)
            self.turtles[index].sety(turtle_ahead_y)

        self.turtles[0].forward(TURTLE_PACE)

    def crash_with_body(self):
        for body_part in self.turtles[1:]:
            if self.head.distance(body_part) < 20:
                print("Snake crashed")
                return True
        return False

    def move_left(self):
        self.turtles[0].setheading(self.turtles[0].heading() + 90)

    def move_right(self):
        self.turtles[0].setheading(self.turtles[0].heading() - 90)

    def grow_snake(self):
        self.turtles.append(_new_box(self.turtles[len(self.turtles) - 1], self.head))
