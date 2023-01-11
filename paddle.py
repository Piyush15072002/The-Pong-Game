# The paddles or bats of the Pong game

from turtle import Turtle

# the dimensions of the paddle are 20x100
# the paddle should be kept at x coordinate -350 and +350, since the screen width is 800 (400 each side)
# so paddle position (350,0) and (-350,0)


class Paddle(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.color(color)
        self.shape("square")    # default size 20x20
        self.shapesize(stretch_wid=5, stretch_len=1)    # 5 x 20 = 100
        self.penup()

        # Since we passed a tuple, so we will pass position like this
        self.goto(position)
        # or
        # self.goto(position[0],position[1])

    
    def Up(self):
        """Function to UP the paddle"""

        # to up, we just have to change the y coordinate
        y = self.ycor() + 40
        self.goto(self.xcor(), y)

    def Down(self):
        """Function to DOWN the paddle"""

        # to down, we just have to change the y coordinate
        y = self.ycor() - 40
        self.goto(self.xcor(), y)

    