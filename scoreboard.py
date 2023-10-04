from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.points = 0

    def update_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.points}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER.", True, align=ALIGNMENT, font=FONT)

    def increase_points(self):
        self.clear()
        self.points += 1
