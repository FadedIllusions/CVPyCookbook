# Import Needed Packages
import cv2


# Load And Display Image
img = cv2.imread("../data/Lena.png")
cv2.imshow("Original", img)
cv2.waitKey(0)


# Save Image With Lower Compression -- Bigger File Size, Faster Decoding
# Value Of IMWRITE_PNG_COMPRESSION Must Be 0-9
# Larger Number, More Compressed, Slower Decoding
cv2.imwrite("output/Lena_Compressed.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

# Load Image To Ensure It Saved, Compare To Original
img_saved = cv2.imread("output/Lena_Compressed.png")
assert img_saved.all() == img.all()

# Save Image In JPEG Format
# Quality Value 0 - 100, With Higher Number Being Of Higher Quality
cv2.imwrite("output/Lena_Compressed.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 0])