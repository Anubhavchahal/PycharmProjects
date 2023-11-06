import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        for row in range(-250, 250, 20):
            self.shape("square")
            self.shapesize(1,2.5)
            self.color(random.choice(COLORS))
            self.penup()
            self.goto(295, row)
            self.forward(-600)
