from turtle import Turtle

class DecorateField(Turtle):
    # turtle to lines on ground

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")

        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.goto(0, -300)

        self.penup()
        self.goto(0, -100)
        self.pendown()
        self.circle(100)

        self.penup()
        self.goto(-400, 300)
        self.pendown()
        self.goto(400, 300)
        self.goto(400, -300)
        self.goto(-400, -300)
        self.goto(-400, 300)
