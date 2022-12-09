# Question 1 
class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print
M.__mro__

# Question 2
from math import pi

class Circle:
    def __init__(self, radius, color):
        self.radius = 1.0
        self.color = "red"
    
    def setRadius(self, radius):
        self.radius = 1.0

    def getRadius(self):
        return self.radius

    def setColor(self, color):
        self.color = "red"

    def getColor(self):
        return self.color

    def toString(self):
        return f"Radius: {self.getRadius()}, Color: {self.getColor()}"

    def getArea(self):
        return self.getRadius() * self.getRadius() * pi

class Cylinder(Circle):
    def __init__(self):
        Circle.__init__(self)

    def getHeight(self):
        return self.height
    
    def setHeight(self, height):
        self.height = 1.0

    def toString(self):
        return f"Height: {self.getHeight()}"

    def getVolume(self):
        return self.getArea() * self.getHeight