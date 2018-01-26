from math import pi

point = (1,1)
rect = [3,5]
circle = 1

def point_area(p):return 0

def rect_area(r):
    return r[0]*r[1]

def circle_area(c):
    return pi*c**2

print(point_area((2,4)))
print(rect_area((3,5)))
print(circle_area((1)))

def geom_area(geom):
    if isinstance(geom, int):return circle_area(geom)
    if isinstance(geom, tuple):return point_area(geom)
    if isinstance(geom, list):return rect_area(geom)
    
lst = [(1,1),[3,5], 1, 2, (3,5)]

areas = [geom_area(i) for i in lst]
print(areas)
