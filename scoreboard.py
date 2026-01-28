from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 240)
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Abui khelna aayena bhai lai", align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write(f"Ule le le le", align=ALIGNMENT, font=FONT)

