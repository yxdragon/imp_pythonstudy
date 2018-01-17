from PIL import Image, ImageFilter

im = Image.open('lena.png')
im2 = im.rotate(45)
im2.show()
