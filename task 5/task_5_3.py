import numpy as np
import matplotlib.pyplot as plt

pmin, pmax, qmin, qmax = -2, 1.5, -1.5, 1.5
ypoints, xpoints = 400, 400
max_i = 50
inf_bolder = 100
image = np.zeros((ypoints,xpoints))

for ip, p in enumerate(np.linspace(pmin, pmax, ypoints)):
    for iq, q in enumerate(np.linspace(qmin, qmax, xpoints)):
        c = p + 1j * q
        z = 0
        for k in range(max_i):
            z = z ** 2 + c
            if abs(z) > inf_bolder:
                image[ip, iq] = 1
                break


plt.axis('off')
plt.imshow(image.T, cmap='Greys')
plt.show()