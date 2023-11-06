from turtle import Screen, Turtle

screen = Screen()
drone = Turtle()

screen.bgcolor("black")
screen.setup(600,600)

def move_turtle():
    drone.shape("turtle")
    drone.color("white")
    drone.penup()
    drone.goto(280,-280)
    drone.pendown()
    for n in range(7):
        if drone.xcor() == 280:
            drone.setheading(90)
            drone.forward(40)
            drone.setheading(180)
            drone.forward(560)
            print(drone.xcor())
        if drone.xcor() == -280:
            drone.setheading(90)
            drone.forward(40)
            drone.setheading(0)
            drone.forward(560)



move_turtle()
screen.exitonclick()