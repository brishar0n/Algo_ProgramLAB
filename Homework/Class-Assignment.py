# Question 1 
# class X:
#     pass

# class Y:
#     pass

# class Z:
#     pass

# class A(X, Y):
#     pass

# class B(Y, Z):
#     pass

# class M(B, A, Z):
#     pass

# print
# M.__mro__

# Question 2
from math import pi

class Circle:
    def __init__(self, radius = 1.0, color = 'red'):
        self.radius = radius
        self.color = color
    
    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"Radius: {self.getRadius()}, Color: {self.getColor()}"

    def getArea(self):
        return self.getRadius() * self.getRadius() * pi

class Cylinder(Circle):
    def __init__(self,radius,color,height=1.0):
        Circle.__init__(self,radius,color)
        self.height = height

    def getHeight(self):
        return self.height
    
    def setHeight(self, height):
        self.height = height

    def toString(self):
        return f"Radius: {self.getRadius()}, Color: {self.getColor()}, Height: {self.getHeight()}"

    def getVolume(self):
        return self.getArea() * self.getHeight()
