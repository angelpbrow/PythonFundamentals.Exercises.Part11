from operator import length_hint
import shapes

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def getArea(self):
        return self.length * self.length

    def getPerimeter(self):
        return 4 * self.length

