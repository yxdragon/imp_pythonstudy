from scipy.misc import imread, imsave
import matplotlib.pyplot as plt
import numpy as np

def autocons(img):
    img-=img.min()
    img = img/img.max()
    return (img*255).astype(np.uint8)

def autoconsS(img):
    img-=img.min()
    img = img/img.max()
    img *= 456
    img -= 100
    img = np.clip(img, 0, 255)
    return img.astype(np.uint8)

img = imread('lena.png')
img = img.mean(axis=2).astype(np.uint8)


img //= 2
img += 128

img2 = autoconsS(img)
imsave('lena2S.png', img2)


#plt.imshow(img, cmap='gray')
#plt.show()
'''
plt.figure()
hist, bins = np.histogram(img, 256, (0, 256))
plt.plot(hist)
plt.show()
'''
'''
img //= 50
img *= 50
plt.imshow(img, cmap='gray')
plt.figure()
hist, bins = np.histogram(img, 256, (0, 256))
plt.plot(hist)
plt.show()
'''
'''
msk = (img>130) * (img<170)
img[msk] = 150
plt.imshow(img)
plt.figure()
hist, bins = np.histogram(img, 256, (0, 256))
plt.plot(hist)
plt.show()

index = np.arange(256)
index[:100] = 0
index[100:200] = 128
index[200:] = 255

img2 = index[img]
plt.imshow(img2, cmap='gray')
plt.show()
'''

'''
img = imread('lena.png')
plt.imshow(img, cmap='gray')

plt.figure()
hist, bins = np.histogram(img, 256, (0, 256))
plt.plot(hist)
plt.show()
'''
