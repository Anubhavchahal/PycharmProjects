# from turtle import Turtle, Screen
# num_sides = 10
# def shape_formation(num_sides):
#     angle = 360/num_sides
#     tim = Turtle()
#     tim.shape("turtle")
#     tim.color("red")
#     for n in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#     screen = Screen()
#     screen.exitonclick()
#
# shape_formation(num_sides)
# # tim = Turtle()
# # tim.shape("turtle")
# # tim.color("red")
# # for n in range(0,5):
# #     tim.forward(100)
# #     tim.right(72)
# #
# # screen = Screen()
# # screen.exitonclick()
# # import heroes
# # for n in range(10):
# #     print(heroes.gen())
# # from turtle import Turtle, Screen
# #
# # tim = Turtle()
# # tim.shape("turtle")
# #
# # for n in range(0,15):
# #     tim.forward(10)
# #     # tim.color("white")
# #     tim.penup()
# #     tim.forward(10)
# #     # tim.color("black")
# #     tim.pendown()
# #
# # screen = Screen()
# # screen.exitonclick()
from turtle import Turtle, Screen
import random

tim = Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for n in range(100):
    tim.forward(30)
    tim.color(random.choice(colours))
    tim.setheading(random.choice([90,180,270,360]))

screen = Screen()
screen.exitonclick()
