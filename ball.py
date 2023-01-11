# the ball for the Pong game

from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        # the ball size if by default 20x20
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(0,0)
        # to move the ball
        self.ballX = 10
        self.ballY = 10
        self.ballSpeed = 0.1 # in time library, this is the time the iteration have to sleep for in seconds

    def move(self):
        """Function to move the ball to top right as default"""

        x = self.xcor() + self.ballX
        y = self.ycor() + self.ballY
        self.goto(x,y)
    
    def bounce(self):
        """Function to bounce the ball"""

        # we just need to reverse Y value, if it is +, then make it -, or vice versa
        # as in maths, to change such value, we use = * -1
        # +10 x -1 = -10 and -10 x -1 = 10
        self.ballY *= -1

    def hit(self):
        """Function to 
        1. bounce back the ball after it make contact with paddle
        2. Increase the speed of the ball"""

        # the logic is same as for bounce() but here we need to reverse the x axis
        self.ballX *= -1

        # increasing speed
        # so in time library, the speed will increase as we decrease the time pause duration
        # it is 0.1, so we need to decrease it to 0.99 to 0.01, but never to a negative value (error)
        # so for this we will multiply it by 0.9

        self.ballSpeed *= 0.9
    
    def reset(self):
        """After the ball is missed, 
        1. To reposition the ball to center  
        2. To serve the ball to opponent
        3. Reset the speed of ball to normal"""

        self.goto(0,0)

        # since someone missed the ball, so now the ball will be served to opponent
        self.ballX *= -1

        # reset speed
        self.ballSpeed = 0.1    # in time library, this is the time the iteration have to sleep for in seconds

