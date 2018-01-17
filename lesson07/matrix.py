import numpy as np
sin, cos = np.sin, np.cos
import matplotlib.pyplot as plt

def scale(s):
    return np.array([[s,0],[0,s]])

def rotate(thi):
    return np.array([[cos(thi), -sin(thi)],
                     [sin(thi), cos(thi)]])

def ellipse(a, b, thi):
    aa = np.linspace(0, np.pi*2, 33)
    pts = np.array([np.cos(aa), np.sin(aa)])
    sca = np.array([[a,0],[0,b]])
    rot = rotate(thi)
    print(rot)
    return np.dot(rot, np.dot(sca, pts))
    
v = np.array([2,3])
print(v)
print(scale(2))
print(np.dot(scale(2),v))

print('')
v = np.array([1,0])
print(v)
print(rotate(np.pi/4))
print(np.dot(rotate(np.pi/4),v))

pts = ellipse(2, 1, np.pi/4)
print(pts.shape)
plt.gca().set_aspect('equal')
plt.plot(pts[0], pts[1])
plt.show()
