from turtle import Turtle


class Separator(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.sety(270)
        self.pendown()
        self.setheading(270)
        self.create()

    def create(self):
        # self.forward(10)
        while self.ycor() != -270:
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()

        self.forward(10)
