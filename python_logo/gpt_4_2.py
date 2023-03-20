import turtle
import math

def draw_snake_part(color, angle):
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.left(angle)
    turtle.circle(100, 180)
    turtle.right(90)
    turtle.forward(200 * math.sin(math.radians(90 - angle)))
    turtle.right(90)
    turtle.circle(100, 180)
    turtle.right(180)
    turtle.end_fill()

def draw_python_logo():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()

    # Draw the left part (blue)
    draw_snake_part('blue', 60)

    # Draw the right part (yellow)
    turtle.right(180)
    draw_snake_part('yellow', 120)

    # Draw the eyes
    turtle.penup()
    turtle.goto(-20, 60)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-180, 60)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    turtle.hideturtle()

# Draw the Python logo using the Turtle library
draw_python_logo()
turtle.done()
