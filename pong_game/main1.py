from turtle import Screen
from paddle1 import Paddle
from ball1 import Ball
import time

screen = Screen()


screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle()
r_paddle.create_paddle((350, 0))
l_paddle = Paddle()
l_paddle.create_paddle((-350, 0))



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle.current_position()) < 50 and ball.xcor() > 320 or ball.distance(l_paddle.current_position()) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()