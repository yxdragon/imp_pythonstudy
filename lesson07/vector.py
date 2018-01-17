import numpy as np

def scaletest():
    a = np.array([1,2])
    b = a*2
    print(a)
    print(b)

def addtest():
    a = np.array([2,3])
    b = np.array([5,5])
    print(a+b)
    print(a-b)

def dottest():
    a = np.array([1,3])
    b = np.array([2,5])
    print(np.dot(a,b))

def crosstest():
    a = np.array([2,0])
    b = np.array([0,5])
    print(np.cross(a,b))
    print(np.cross(b,a))
    
scaletest()
addtest()
dottest()
crosstest()
