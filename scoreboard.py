from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.showscore()
        self.hideturtle()

    def showscore(self):
        self.write(f"Score: {self.score}            High Score: {self.highscore}", align="center", font=("Ariel", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.showscore()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.showscore()

   