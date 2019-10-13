# Import Needed Packages
import numpy as np
import cv2


# Load Image As Grayscale, Convert To A 32b Float And Scale
image = cv2.imread('../data/Lena.png',0).astype(np.float32)/255

# Implement Gamma Correction
gamma = 0.5
image_corrected = np.power(image, gamma)

# Display Original And Corrected Images
cv2.imshow("Original", image)
cv2.imshow("Corrected", image_corrected)
cv2.waitKey(0)

# Scale and Save Images
cv2.imwrite('tmp/image.png', image*255)
cv2.imwrite('tmp/image_corrected.png', image_corrected*255)

# Cleanup
cv2.destroyAllWindows()