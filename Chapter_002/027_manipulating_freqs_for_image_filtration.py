# In The Following, We're To Convert The Input Image From The Spatial Domain
# Into The Frequency Domain, Center Low Frequencies, Take An Inverted Mask Of
# Low Freqs (So, High Frequencies Only)... Thus, Our Filtered Image Will Allow
# Only High Freqs To Pass, Giving Us The Edges Within The Image

# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import cv2


# Load (FS), Convert, Scale Image
image = cv2.imread('../data/Lena.png', 0).astype(np.float32)/255

# Apply Discrete Fourier Transform
fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift FFT In Such A Way That Low Frequencies Are Located At Center
fft_shift = np.fft.fftshift(fft, axes=[0,1])

# Set Amplitudes For High Freqs To Zero
sz = 25
mask = np.zeros(fft.shape, np.uint8)
mask[image.shape[0]//2-sz:image.shape[0]//2+sz, image.shape[1]//2-sz:image.shape[1]//2+sz, :] = 1
# Take Inverse Of Mask (High Freqs Only)
fft_shift *= 1-mask

# Shift DFT Back
fft = np.fft.ifftshift(fft_shift, axes=[0,1])

# Convert Back To Spatial Domain
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

cv2.imshow("Original", image)
cv2.imshow("Filtered", filtered)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()