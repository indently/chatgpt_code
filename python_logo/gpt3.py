import turtle

# set up the turtle screen
turtle.bgcolor("white")
turtle.speed(0)

# define a function to draw a square
def square(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

# draw the yellow square
square(200, "#FFD43B")

# draw the inner blue squares
turtle.penup()
turtle.goto(-90, 90)
turtle.pendown()
square(60, "#3776AB")

turtle.penup()
turtle.goto(30, 90)
turtle.pendown()
square(60, "#3776AB")

# draw the outer blue squares
turtle.penup()
turtle.goto(-110, 70)
turtle.pendown()
square(100, "#2C3E50")

turtle.penup()
turtle.goto(10, 70)
turtle.pendown()
square(100, "#2C3E50")

# hide the turtle and exit the program
turtle.hideturtle()
turtle.done()
