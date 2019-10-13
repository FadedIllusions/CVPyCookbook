# Import Needed Packages
import numpy as np
import cv2


# Create Matrix With Random Values, 100x100
mat = np.random.rand(100,100).astype(np.float32)
print("Shape: ", mat.shape)
print("Data Type: ", mat.dtype)

# Save Random Matrix To File
np.savetxt('mat.csv', mat)

# Load It From File
# Print Shape And Type
mat_2 = np.loadtxt('mat.csv').astype(np.float32)
print("Shape: ", mat_2.shape)
print("Data Type: ", mat_2.dtype)


# If Curious, Display As Image
cv2.imshow("Mat", mat)
cv2.imshow("Mat 2", mat_2)
cv2.waitKey(0)