from turtle import Turtle
import time


class Player(Turtle):
    def __init__(self, x):
        super().__init__()
        self.speed('fastest')
        self.x_cor = x
        self.penup()
        self.shape('square')
        self.color('white')
        self.teleport(x, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() != 240:
            y = self.ycor() + 20
            self.teleport(self.x_cor, y)

    def go_down(self):
        if self.ycor() != -240:
            y = self.ycor() - 20
            self.teleport(self.x_cor, y)
