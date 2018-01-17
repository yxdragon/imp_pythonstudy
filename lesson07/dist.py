import numpy as np
from numpy.linalg import norm

def dist(p1,p2,p3,p4):
    p1, p2, p3, p4 = np.array([p1,p2,p3,p4])
    v1, v2 = p2-p1, p4-p3
    vt = np.cross(v1, v2)
    return abs(np.dot(p3-p1, vt)/norm(vt))

print(dist((0,0,0),(1,0,0), (0,0,1),(0,1,1)))
