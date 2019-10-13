# Gabor Filters Are, Generally, Used In Texture Analysis, Edge Detection, Feature 
# Extraction, Disparity Estimation (In Stereo Vision), Etc. 
#
# Gabor Filters Are Special Classes Of Bandpass Filters, I.E...
# They Allow A Certain ‘Band’ Of Frequencies And Reject The Others.

# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import cv2


# Read In Image As Grayscale, Convert, Scale
image = cv2.imread('../data/Lena.png', 0).astype(np.float32)/255

# Construct Real-Valued Filter Kernel
# Normalize Such That It Has An L2 Unit Norm
# cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)
kernel = cv2.getGaborKernel((21,21), 5, 1, 10, 1, 0, cv2.CV_32F)
kernel /= np.sqrt((kernel * kernel).sum())

# Filter Image
filtered = cv2.filter2D(image, -1, kernel)

# Display Original And Filtered Images
cv2.imshow("Original", image)
cv2.imshow("Kernel", kernel)
cv2.imshow("Filtered", filtered)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()