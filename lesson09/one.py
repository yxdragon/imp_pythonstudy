import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import convolve1d

#data = np.array([80,85,91,88,30,85,93,88])
data = np.array([20,25,23,30,45,70,80,88,90,88,70,86,90])
#                0.3 0.3 0.3
plt.plot(data, 'g')
data2 = data.copy()
data2[:] = data.mean()
plt.plot(data2, 'r')
data3 = convolve1d(data, [1/3.0]*3)
plt.plot(data3, 'b')
#plt.show()

plt.figure()
data = [7,10,12,15,25,28,30,28,10,5,3,0]
plt.plot(data, 'g')
data2 = convolve1d(data, [1,-1])
print(data2)
print(np.argmax(data2), np.argmin(data2))
plt.plot(data2, 'r')
plt.show()
