from PIL import Image, ImageOps
import matplotlib.pyplot as plt 
import numpy as np


face = Image.open('task 3/data/face.jpg').convert('L')
crop_face = ImageOps.fit(face,(100,100))

round_face = np.array(face)
sy, sx = round_face.shape
y, x = np.ogrid[0:sy, 0:sx]

centerx, centery = (450, 400)
mask = ((y - centery)**2 + (x - centerx)**2) > 550**2
round_face[mask] = 0

columns = 4
rows = 1

fig = plt.figure()

fig.add_subplot(rows, columns, 1)
plt.imshow(face, cmap='gray')
plt.axis('off')

fig.add_subplot(rows, columns, 2)
plt.imshow(face, cmap='pink')
plt.axis('off')

fig.add_subplot(rows, columns, 3)
plt.imshow(crop_face)
plt.axis('off')

fig.add_subplot(rows, columns, 4)
plt.imshow(round_face)
plt.axis('off')
plt.show()
