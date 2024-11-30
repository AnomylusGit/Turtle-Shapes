import turtle
turtle.Screen().bgcolor("red")

sc = turtle.Turtle()
turtle.title("Turtle Usage")
#star
#triangle1
sc.forward(100)

sc.left(110)
sc.forward(100)

sc.left(130)
sc.forward(100)
sc.penup()
sc.right(150)
sc.forward(50)
#triangle2
sc.pendown()
sc.right(90)
sc.forward(100)

sc.right(110)
sc.forward(100)

sc.right(120)
sc.forward(100)
turtle.done()