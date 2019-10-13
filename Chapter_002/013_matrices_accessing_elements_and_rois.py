# Being As Images Are Represented As Matrices,
# We Can Act Upon Them As Such

# Import Needed Packages
import numpy as np
import cv2


# Draw A White Background, 640x480 (BGR)
image = np.full((480,640,3), 255, np.uint8)
cv2.imshow("White", image)
cv2.waitKey(0)

# Draw A Red Background, 640x480 (BGR)
image = np.full((480,640,3), (0,0,255), np.uint8)
cv2.imshow("Red", image)
cv2.waitKey(0)

# Draw A Black Background By Filling Previous Background
# 640x480 (BGR)
image.fill(0)
cv2.imshow("Black", image)
cv2.waitKey(0)

# Draw Three White Sections In Previous (Black) Image
image[240,160] = image[240,320] = image[240,480] = (255,255,255)
cv2.imshow("Black And White", image)
cv2.waitKey(0)

# Replace Previous Black Sections With Blue
# Black Represented By '0'. If We Put Blue Layer At 255,
# We Get (255,0,0) -- Blue
image[:,:,0] = 255
cv2.imshow("Blue And White", image)
cv2.waitKey(0)

# Draw Vertical White Line Through 320 Column
image[:,320,:] = 255
cv2.imshow("Blue With White Line", image)
cv2.waitKey(0)

# Add Red To ROI
# Making ROI (255,0,255)
image[100:600, 100:200, 2] = 255
cv2.imshow("ROI", image)
cv2.waitKey(0)


# Cleanup
cv2.destroyAllWindows()