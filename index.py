import turtle

def cuadrado_simple():
    obj = turtle.Turtle()

    for i in range(4):
        obj.forward(100)
        obj.right(90)

    turtle.done()


def tablero():
    ventana = turtle.Screen()
    tortuga = turtle.Turtle()
    tortuga.forward(300)
    tortuga.left(90)
    tortuga.forward(300)
    tortuga.left(90)
    tortuga.forward(300)
    tortuga.left(90)
    tortuga.forward(300)
    tortuga.left(90)
    penup()
    tortuga.forward(100)
    tortuga.left(90)
    pendown()
    tortuga.forward(100)
    


    ventana.mainloop()


tablero()


