# Equalizing Histogram Enhances Contrast

# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import cv2


# Read In Image As Grayscale
gray = cv2.imread('../data/Lena.png', 0)

# Equalize Histogram
equalized = cv2.equalizeHist(gray)

# Define Histogram And Display
hist, bins = np.histogram(equalized, 256, [0,255])
plt.fill_between(range(256), hist, 0)
plt.title("Equalized GS Histogram")
plt.xlabel("Pixel Value")
plt.show()

# Display Original And Equalized Image
cv2.imshow("Original -- GS", gray)
cv2.imshow("Equalized -- GS", equalized)
cv2.waitKey(0)


# Load Image As BGR, Convert To HSV
bgr = cv2.imread('../data/Lena.png')
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

# Equalize 'Value' (Channel) Of HSV
hsv[...,2] = cv2.equalizeHist(hsv[...,2])
equalized = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Display BGR And Equalized Images
cv2.imshow("BGR", bgr)
cv2.imshow("BGR Eq V", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()