from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

h = -100
for n in colors:
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.goto(x=-230, y= h)
    timmy.color(n)
    h += 50
    all_turtles.append(timmy)

print(all_turtles)
screen.exitonclick()