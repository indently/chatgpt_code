import turtle


def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


turtle.speed(0)

# Draw the blue circle
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
draw_circle(100, 'blue')

# Draw the yellow circle
turtle.penup()
turtle.goto(0, -70)
turtle.pendown()
draw_circle(70, 'yellow')

# Draw the green circle
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
draw_circle(80, 'green')

# Draw the red circle
turtle.penup()
turtle.goto(0, -90)
turtle.pendown()
draw_circle(90, 'red')

turtle.hideturtle()
turtle.done()
