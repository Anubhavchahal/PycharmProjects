from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = Turtle()

    def create_paddle(self, position):
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(position)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        new_x = self.paddle.xcor()
        self.paddle.speed("fastest")
        self.paddle.goto(new_x, new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        new_x =self.paddle.xcor()
        self.paddle.speed("fastest")
        self.paddle.goto(new_x, new_y)

    def current_position(self):
        return (self.paddle.xcor(), self.paddle.ycor())


