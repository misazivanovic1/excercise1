import turtle


pen = turtle.Turtle()


def drawing():
    pen.fd(100)

def sqr(value):
    for x in range(4):
        pen.fd(value)
        pen.left(90)

def shape(distance,num):
    angle = 360/num
    for x in range(num):
        pen.fd(distance)
        pen.left(angle)

shape(100,4)
shape(100,3)
shape(100,5)
shape(100,8)


turtle.done()