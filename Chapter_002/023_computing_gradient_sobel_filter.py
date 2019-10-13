# OpenCV's cv2.Sobel Function Computes Image Gradient Approximation
# Using A Linear Filter Of A Specified Size. Through Function Parameters,
# You Can Specify Exactly Which Derivative Needs To Be Used.

# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import cv2


# Read In Image As Grayscale,
image = cv2.imread('../data/Lena.png', 0)

# Create Sobel X And Y Filters
sx = cv2.Sobel(image, cv2.CV_32F, 1, 0)
sy = cv2.Sobel(image, cv2.CV_32F, 0, 1)

# 
plt.figure(figsize=(8,3))
plt.subplot(131)
plt.axis('off')
plt.title('image')
plt.imshow(image, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.imshow(sx, cmap='gray')
plt.title(r'$frac{dI}{sx}$')
plt.subplot(133)
plt.axis('off')
plt.title(r'$frac{dI}{sy}$')
plt.imshow(sy, cmap='gray')
plt.tight_layout()
plt.show()