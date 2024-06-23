import turtle

class LovellyShapes():
    def __init__(self, lenght, num):
        self.lenght = lenght
        self.num = num
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.angle = 360/self.num

    def shape(self):
        for x in range(self.num):
            self.pen.fd(self.lenght)
            self.pen.left(self.angle)

    def move(self,x,y):
        self.pen.penup()
        self.pen.goto(x,y)
        self.pen.pendown()

    def funnyshape(self):
        for y in range(self.lenght):
            for x in range(self.num):
                self.pen.fd(y)
                self.pen.left(self.angle+2)

sqr = LovellyShapes(100,4)
trgl = LovellyShapes(100,3)
circle = LovellyShapes(100,360)

sqr.shape()
trgl.move(0,100)
trgl.shape()

circle.move(200,-200)
sqr.move(-150,-150)
trgl.move(200,200)
#sqr.funnyshape()
#trgl.funnyshape()
circle.funnyshape()


turtle.done()