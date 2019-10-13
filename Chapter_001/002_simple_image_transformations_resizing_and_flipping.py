# Usage:
# python 002_simple_image_transformations_resizing_and_flipping.py --image ../data/Lena.png


# Import Needed Packages
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Input Image")
args = vars(ap.parse_args())


# Load Image From Disk
img = cv2.imread(args["image"])

# Print Original Size/Shape
print("\n---   ---   --- # # # RESIZING # # # ---   ---   ---")
print("Original Image Shape: ", img.shape)


# OpenCV Offers Several Ways To Use cv2.resize Function
#
# We Can Set The Target Size (Width, Height) In Pixels
width, height = 128, 256
img_resized = cv2.resize(img, (width,height))
print("Resized To 128x256 Image Shape: ", img_resized.shape)

# Resize By Setting Multipliers
w_mult, h_mult = 0.25, 0.5
img_resized = cv2.resize(img, (0,0), img_resized, w_mult, h_mult)
print("Resized By Mulitpliers Shape: ", img_resized.shape)

# Resize (Enlarge) Using Nearest-Neighbor Interpolation
w_mult, h_mult = 2, 4
img_resized = cv2.resize(img, (0,0), img_resized, w_mult, h_mult, cv2.INTER_NEAREST)
print("Nearest Neighbor Image Shape: ", img_resized.shape, "\n")


# Flip/Reflect Along Horizontal X-Axis
img_flip_x = cv2.flip(img, 0)

# Flip Vertically Along Y-Axis
img_flip_y = cv2.flip(img, 1)

# Flip XY-Axis Simultaneously
img_flip_xy = cv2.flip(img, -1)

# Display Original And Flipped Images
cv2.imshow("Original", img)
cv2.imshow("Flip X-Axis", img_flip_x)
cv2.imshow("Flip Y-Axis", img_flip_y)
cv2.imshow("Flip XY-Axis", img_flip_xy)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()