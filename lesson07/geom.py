import numpy as np
import matplotlib.pyplot as plt

def triarea(p1, p2, p3):
    v1 = np.array(p2)-np.array(p1)
    v2 = np.array(p3)-np.array(p1)
    return np.abs(np.cross(v1, v2)/2)

def polyarea(pts):
    return np.abs(np.cross(pts[:-1], pts[1:]).sum())/2
    
    
print(triarea((0,0),(2,0),(1,1)))
a = np.linspace(0, np.pi*2, 10000)
xs, ys = np.cos(a), np.sin(a)

print(polyarea(np.array([xs, ys]).T))
plt.gca().set_aspect('equal')
plt.plot(xs, ys)
plt.show()
