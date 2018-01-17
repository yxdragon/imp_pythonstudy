from scipy.misc import imread
import matplotlib.pyplot as plt

arr = imread('lena.png')
plt.imshow(arr)
plt.show()

plt.imshow(arr[:,::-1])
plt.show()

plt.imshow(arr[::8,::8])
plt.show()

arr[:100,:100,0] //= 2
arr[100:200,100:200,1] = 255
arr[200:300,200:300,2] = 255
plt.imshow(arr)
plt.show()
