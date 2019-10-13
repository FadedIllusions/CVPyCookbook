# You Can Think Of Frequency In An Image As The Rate Of Change. Parts Of The Image 
# That Change Rapidly From One Color To Another (Sharp Edges) Contain High Frequencies
# And Parts That Change Gradually (E.G., Large Surgaces With Solid Colors) Contain 
# Only Low Frequencies

# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import cv2


# Load Image As GS, Convert, Scale
image = cv2.imread('../data/Lena.png', 0).astype(np.float32)/255

# Apply Discrete Fourier Transform
# Print Shape And Data Type
fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)
print("FFT Shape: ", fft.shape)
print("FFT DType: ", fft.dtype)

# Visualize Image Spectrum
# Shift In Such A Way That The Amplitude Corresponding To Zero
# Frequency Becomes Located At Center Of Image
shifted = np.fft.fftshift(fft, axes=[0,1])
magnitude = cv2.magnitude(shifted[:,:,0], shifted[:,:,1])
magnitude = np.log(magnitude)
magnitude -= magnitude.min()
magnitude /= magnitude.max()

# Convert From Frequency Spectrum Back To Spatial Representation
restored = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

cv2.imshow("Image", image)
cv2.imshow("Magnitude", magnitude)
cv2.imshow("Restored", restored)
cv2.waitKey(0)