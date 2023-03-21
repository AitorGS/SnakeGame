from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(-40, 280)
        self.style = ('arial', 12)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score:\t{self.score}", font=self.style )

    def increase_score(self):
        self.score += 1
        self.show_score()

    @staticmethod
    def game_over():
        game_over_message = Turtle()
        game_over_message.color("white")
        game_over_message.penup()
        game_over_message.hideturtle()
        game_over_message.setposition(-60, 0)
        game_over_message.style = ("arial", 18)
        game_over_message.write("Game over", font=game_over_message.style)




