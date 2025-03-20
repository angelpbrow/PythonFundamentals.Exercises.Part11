from operator import length_hint
import shapes

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        print (self.length * self.width)

    def getPerimeter(self):
        print (2 * (self.length + self.width))

class Square(Rectangle):
    def __init__(self, length):
            self.length = length
            self.width = length

    def getArea(self):
            print( self.length * self.width)

    def getPerimeter(self):
            print (4 * self.length)


#rect = shapes.Rectangle(2,4)
#rect.getArea()

squ = shapes.Square(2)
squ.getPerimeter(2)


