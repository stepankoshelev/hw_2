import turtle

def nested():
    type1 = 5
    for i in range(10):
        for i in range(5):
            turtle.forward(type1)
            turtle.left(90)
        turtle.penup()
        turtle.right(180)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.pendown()
        type1 = type1 +50



iа__name__== "  main  "
    nested
    while True:
        pass
turtle.done()
