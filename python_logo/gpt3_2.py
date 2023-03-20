import turtle

# set up the turtle screen
turtle.bgcolor("#FFD43B")
turtle.speed(0)

# draw the outer circle
turtle.penup()
turtle.goto(0, -120)
turtle.pendown()
turtle.color("#3776AB")
turtle.begin_fill()
turtle.circle(120)
turtle.end_fill()

# draw the inner circle
turtle.penup()
turtle.goto(0, -95)
turtle.pendown()
turtle.color("#FFFFFF")
turtle.begin_fill()
turtle.circle(95)
turtle.end_fill()

# draw the snake
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("#000000")
turtle.pensize(25)
turtle.right(45)
turtle.circle(70, 270)

# draw the eye
turtle.penup()
turtle.goto(-30, 30)
turtle.pendown()
turtle.color("#FFFFFF")
turtle.begin_fill()
turtle.circle(12)
turtle.end_fill()

# draw the pupil
turtle.penup()
turtle.goto(-25, 35)
turtle.pendown()
turtle.color("#000000")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# hide the turtle and exit the program
turtle.hideturtle()
turtle.done()
