# Score record

from turtle import Turtle

class Score(Turtle):

    def __init__(self):

        super().__init__()

        self.color("lime green")
        self.penup()
        self.hideturtle()

        self.leftPlayer = 0
        self.rightPlayer = 0

        self.A = "Player A"
        self.B = "Player B"

        self.showScore()


    def showScore(self):
        
        self.clear()
    
        self.goto(-100, 275)
        self.write(self.A, align="center", font=("Simsun", 15, "normal"))
        self.goto(-100,230)
        self.write(self.leftPlayer, align="center", font=("Simsun", 30, "normal"))

        self.goto(100, 275)
        self.write(self.B, align="center", font=("Simsun", 15, "normal"))
        self.goto(100,230)
        self.write(self.rightPlayer, align="center", font=("Simsun", 30, "normal"))




    def updateLeftScore(self):

        self.leftPlayer += 1
        self.showScore()
        

    def updateRightScore(self):

        self.rightPlayer += 1
        self.showScore()
        