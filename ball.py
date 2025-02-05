from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(20)
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)


    def bounce(self):
        self.y_move *= -1

    def bounce_off_player(self):
        self.x_move *= -1
