from operator import length_hint


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self, length, width):
        area = length * width
        print (area)

    def getPerimeter(self,length, width):
        perimeter = 2 * (length + width)
        print (perimeter)


Rectangle.getArea(0,4,8)
Rectangle.getPerimeter(Rectangle,4,3)
