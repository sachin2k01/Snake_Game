from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score{self.score}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!", align=ALLIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 10
        self.clear()
        self.update_score()


