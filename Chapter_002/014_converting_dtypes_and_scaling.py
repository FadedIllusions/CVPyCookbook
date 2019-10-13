# Import Needed Packages
import numpy as np
import cv2

# Load And Display Image
image = cv2.imread('../data/Lena.png')
print("Shape: ", image.shape)
print("Data Type: ", image.dtype)
cv2.imshow("Original", image)
cv2.waitKey(0)

# Convert To Float32 dType
# Scale To Range Of [0,1] -- Divide By 255
# This Will Leave You With Original Image
# Display Converted And Scaled Image
image = image.astype(np.float32)/255
print("Shape: ", image.shape)
print("Data Type: ", image.dtype)
cv2.imshow("Converted And Scaled", image)
cv2.waitKey(0)

# Multiply By 2, Clip/Scale To Range [0,1]
#Display Newly Scaled Image
# Note:
# Multiplying By Two Will Increase Brightness
# If 0 Darkest, 1 Lightest
# Mid-Value: 0.5
# Mid * 2 = 0.5 * 2 = 1 ...
cv2.imshow("... Again", np.clip(image*2, 0, 1))
cv2.waitKey(0)

# Convert Back To Range [0,255]
# Convert Back To An Unsigned 8-Bit Integer
# Display Image
image = (image*255).astype(np.uint8)
print("Shape: ", image.shape)
print("Data Type: ", image.dtype)
cv2.imshow("Converted Back", image)
cv2.waitKey(0)
cv2.destroyAllWindows()