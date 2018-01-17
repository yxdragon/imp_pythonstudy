from skimage.data import coins
import matplotlib.pyplot as plt
import numpy as np

from scipy.ndimage import uniform_filter, gaussian_filter, sobel

img = coins()
'''
plt.imshow(img, cmap='gray')
img2 = uniform_filter(img, 8)
plt.figure()
plt.imshow(img2, cmap='gray')
img3 = gaussian_filter(img, 8)
plt.figure()
plt.imshow(img3, cmap='gray')
plt.show()
'''

plt.imshow(img, cmap='gray')
img2 = uniform_filter(img, 8)
plt.figure()
img = img.astype(np.int16)
imgh = np.abs(sobel(img, axis=1))
plt.imshow(imgh, cmap='gray')
plt.figure()
imgv = np.abs(sobel(img, axis=0))
plt.imshow(imgv, cmap='gray')
plt.figure()
imgh = imgh.astype(np.float)
imgv = imgv.astype(np.float)
imghv = np.sqrt(imgh**2+imgv**2)
plt.imshow(imghv, cmap='gray')
plt.show()
