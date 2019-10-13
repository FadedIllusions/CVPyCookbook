# Import Needed Packages
import cv2


# Load Image (BGR) And Display
image = cv2.imread('../data/Lena.png')
img = image.copy()
cv2.imshow("BGR", image)
cv2.waitKey(0)

# Convert To Grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", image)
cv2.waitKey(0)

# Convert Back To BGR
# GS Is A Single Channel
# ... Will We Be Able To Convert Back To BGR (3 Channels)?
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.imshow("BGR Maybe", image)
cv2.waitKey(0)

# BGR
cv2.imshow("BGR!", img)
cv2.waitKey(0)

# Convert To HSV
image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", image)
cv2.waitKey(0)

# Now, Convert Back To BGR And Display
image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imshow("BGR", image)
cv2.waitKey(0)


# Cleanup
cv2.destroyAllWindows()