# Learn To Deal WIth Matrix Channels, Access Individual Channels,
# Swap Channels, Perform Algebraic Operations, Etc


# Import Needed Packages
import numpy as np
import cv2


# Load Image, Scale, Print Shape
image = cv2.imread("../data/Lena.png").astype(np.float32)/255
print("Shape: ", image.shape)

# Display Image
cv2.imshow("Original", image)
cv2.waitKey(0)

# Swap B And R Channels
image[:,:,[0,2]] = image[:,:,[2,0]]
cv2.imshow("B And R Swap", image)
cv2.waitKey(0)

# Switch B And R Channels Back (BGR)
# Slightly Tone Down Blue And Scale
image[:,:,[0,2]] = image[:,:,[2,0]]
image[:,:,0] = (image[:,:,0] * 0.9).clip(0,1)
cv2.imshow(" ", image)
cv2.waitKey(0)