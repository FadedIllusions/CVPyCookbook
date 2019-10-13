# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import cv2


# Read in Image, Convert To Float, Scale
image = cv2.imread('../data/Lena.png').astype(np.float32)/255

# Add Noise And Display
noise = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noise = noise.clip(0,1)
plt.imshow(noise[:,:,[2,1,0]])
plt.show()

# Remove Noise With Gaussian Blur
gauss = cv2.GaussianBlur(noise, (7,7), 0)
plt.imshow(gauss[:,:,[2,1,0]])
plt.show()

# Remove Noise With Median Blur
median = cv2.medianBlur((noise*255).astype(np.uint8), 7)
plt.imshow(median[:,:,[2,1,0]])
plt.show()

# Remove Noise With Bilateral Filter
bilat = cv2.bilateralFilter(noise, -1, 0.3, 10)
plt.imshow(bilat[:,:,[2,1,0]])
plt.show()