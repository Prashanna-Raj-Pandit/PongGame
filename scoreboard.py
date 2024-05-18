import random
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self,name,x_co,y_co):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x_co, y_co)
        self.print_score(name)

    def print_score(self,name):
        self.write(f"Player {name}: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self,name):
        self.clear()
        self.score += 1
        self.print_score(name)

