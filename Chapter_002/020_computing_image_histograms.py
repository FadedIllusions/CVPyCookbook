# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import cv2


# Read In Image As Grayscale And Display
gray = cv2.imread('../data/Lena.png', 0)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)

# Define Histogram
hist, bins = np.histogram(gray, 256, [0,255])

# Plot Histogram And Display
plt.fill(hist)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Value")
plt.show()