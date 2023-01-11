# This is the famous PONG game project

import random
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
from decorateField import DecorateField

# Sreen setup

screen = Screen()

screen.bgcolor("black")

# The dimensions of the screen are 800x600
screen.setup(width=800 , height=600)

screen.title("The Pong Game") 

# To avoid turtle creation animation
screen.tracer(0)    # 0 means off, now update the screen








#! Creating objects

# Setting up the field
field = DecorateField()

# paddles
paddleLeft = Paddle((-350, 0), "navy")
paddleRight = Paddle((350, 0), "red")

# ball
ball = Ball()

# score
score = Score()



#! Listening to events

screen.listen()

screen.onkey(paddleLeft.Up, "w")
screen.onkey(paddleLeft.Down, "s")

screen.onkey(paddleRight.Up, "Up")
screen.onkey(paddleRight.Down, "Down")


gameOn = True


while gameOn:

    # Since the ball is moving too fast, so we will use the time function to slow it down
    time.sleep(ball.ballSpeed) # this will make the while loop stop for 0.1 second after each iteration

    screen.update()

    ball.move()

    # detect collision with the wall

    # since the y axis is (-300, 300) and it is the wall for the ball
    if ((ball.ycor() > 280) or (ball.ycor() < -280)):
        ball.bounce()

    # detecting collision with the paddles

    if ( ((ball.distance(paddleRight) < 40) and (ball.xcor() > 320))  or  ((ball.distance(paddleLeft) < 40) and (ball.xcor() < -320)) ):
        
        ball.hit()

    
    # to detect if someone misses the ball  

    if (ball.xcor() > 390):     # Right

        ball.reset()

        # if the right missed, point goes to left
        score.updateLeftScore()
    

    if (ball.xcor() < -390):    # Left

        ball.reset()

        # if the left missed, point goes to right
        score.updateRightScore()




screen.exitonclick()