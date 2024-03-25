import turtle as t
from turtle import Screen
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
# First Challenge DRAW a square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)


# Second challenge - DRAW a dashed line
# for i in range(50):
#     timmy_the_turtle.fd(10)
#     timmy_the_turtle.dot(10, "white")
#     timmy_the_turtle.fd(10)
#     if i % 5 == 0:
#         timmy_the_turtle.right(90)
#
#
#


# Third challenge - DRAW all the shapes mentioned in task

colours = ["green", "red", "blue", "yellow", "black", "wheat", "grey", "orange"]

#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)

# Fourth challenge - random walk
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(200):
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))

# Fifth challenge - Draw a Spirograph
#
# screen = Screen()
# timmy_the_turtle = t.Turtle()
# screen.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# timmy_the_turtle.speed("fastest")
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy_the_turtle.color(random_color())
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
#
#
# draw_spirograph(5)

# Final task = hirstpainting
screen = Screen()
screen.colormode(255)

timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy_the_turtle.dot(20, random.choice(color_list))
    timmy_the_turtle.forward(50)

    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)










screen = Screen()
screen.exitonclick()