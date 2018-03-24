import numpy as np
import matplotlib.pyplot as plt

from skimage.data import camera
from skimage.filters import roberts, sobel, scharr, prewitt
from skimage import io

image_path1 = 'c:/Users/bunny/Desktop/test1.jpg'
image_path2 = 'c:/Users/bunny/Desktop/test2.jpg'
image1 = io.imread(image_path1, as_grey=True)
image2 = io.imread(image_path2, as_grey=True)
edge_roberts1 = prewitt(image1)
edge_roberts2 = prewitt(image2)
# edge_sobel = sobel(image)

fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
                       figsize=(8, 4))

ax[0].imshow(edge_roberts1, cmap=plt.cm.gray)
ax[0].set_title('Roberts Edge Detection')

ax[1].imshow(edge_roberts2, cmap=plt.cm.gray)
ax[1].set_title('Sobel Edge Detection')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
