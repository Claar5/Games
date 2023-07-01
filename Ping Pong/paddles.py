from turtle import Turtle


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.createPaddle(position)

    def createPaddle(self, position):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.color("white")
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
