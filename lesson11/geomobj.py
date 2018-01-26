from math import pi

class Geometry:
    def printself(self):print('I am a geometry')
    def area(self):print('I am a geometry')

class Point(Geometry):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printself(self):
        print('point:%s,%s'%(self.x, self.y))

    def area(self):return 0

class Rect(Geometry):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def printself(self):
        print('rect:%s,%s'%(self.w, self.h))

    def area(self):return self.w * self.h

class Circle(Geometry):
    def __init__(self, r):
        self.r = r

    def printself(self):
        print('circle:%s'%(self.r))

    def area(self):return pi*self.r**2

lst = [Point(0,0), Rect(3,5), Circle(1)]
rst = [i.area() for i in lst]
