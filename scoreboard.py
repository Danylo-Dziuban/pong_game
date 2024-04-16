from turtle import Turtle

FONT = ('Courier', 30, 'normal')
ALIGNMENT = 'center'


class ScoreBoard(Turtle):
    def __init__(self, position, player):
        super().__init__()
        self.player = player
        self.hideturtle()
        self.penup()
        self.score = 0
        self.setpos(position)
        self.color('white')
        self.write(f"{self.score}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER. {self.player} WON", False, ALIGNMENT, FONT)
