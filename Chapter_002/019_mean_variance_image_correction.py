# Import Needed Packages
import numpy as np
import cv2


# Load Image, Convert To Float, Scale [0,1]
image = cv2.imread('../data/Lena.png').astype(np.float32)/255

# Display Original Image
cv2.imshow("Original", image)

# Subtract Mean, Divide By Standard Deviation
# Can Also Use cv2.meanStdDev()
image -= image.mean()
image /= image.std()

# Display Standardized Image
cv2.imshow("Standardized", image)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()