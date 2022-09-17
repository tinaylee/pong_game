from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color("white")

    def display_score(self):
        self.clear()
        self.write(self.score, font=("Courier", 60, "bold"))

    def increment_score(self):
        self.score += 1
        self.display_score()
