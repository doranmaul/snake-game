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
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.points} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.points = 0
        self.update_score()

    def increase_points(self):
        self.points += 1
