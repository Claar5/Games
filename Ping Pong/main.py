# create the screen
# create and move the paddle
# create another paddle
# create and make the ball move
# detect collision with wall and bounce
# detect collision with the paddle
# detect when ball misses the paddle
# keep score
import time
from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")

paddle1 = Paddles((-360, 0))
paddle2 = Paddles((360, 0))

screen.listen()

screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

ball = Ball()
scoreboard = Scoreboard()


while True:
    ball.move()
    time.sleep(ball.move_speed)
    # collision with sides
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # collisions with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() < -330 or ball.distance(paddle2) < 50 and ball.xcor() > 330:
        ball.bounce_x()


    # if ball is missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.lpoint()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rpoint()












screen.exitonclick()
