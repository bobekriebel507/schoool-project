import turtle
screen = turtle.Screen()
kai = turtle.Turtle()
turtle.bgcolor("black")
screen.setup(600, 400)
kai.penup()
kai.goto(-150, -250)
kai.color("white")
kai.pendown()

for i in range(9):
    kai.forward(80)
    kai.right(45)

screen.exitonclick()
