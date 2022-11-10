from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f'Level: {self.score} ', align='left', font=FONT)

    def score_a_point(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=FONT)