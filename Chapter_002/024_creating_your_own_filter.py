# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import math
import cv2


# Read In Image
image = cv2.imread('../data/Lena.png')

# Create An 11x11 Sharpening Kernel
kSize = 11
alpha = 2

kernel = cv2.getGaussianKernel(kSize,0)
kernel = -alpha * kernel @ kernel.T
kernel[kSize//2, kSize//2] += 1 + alpha

# Filter Image Using Created Kernel
filtered = cv2.filter2D(image, -1, kernel)

# Display Results
plt.figure(figsize=(8,4))
plt.subplot(121)
plt.axis('off')
plt.title('Image')
plt.imshow(image[:,:,[2,1,0]])
plt.subplot(122)
plt.axis('off')
plt.title('Filtered')
plt.imshow(filtered[:,:,[2,1,0]])
plt.tight_layout(True)
plt.show()