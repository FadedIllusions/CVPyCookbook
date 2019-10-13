# Usage:
# python 001_reading_images_from_file.py --image ../data/Lena.png


# Import Needed Packages
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Input Image")
args = vars(ap.parse_args())


# Load Image From Disk
img = cv2.imread(args["image"])

# Check If Image Successfully Loaded
assert img is not None

# Display Info About Image
print("\nRead {}".format(args["image"]))
print("Shape: ", img.shape)
print("dytype: ", img.dtype)


# Load Image As Grayscale
img = cv2.imread(args["image"], 0)
assert img is not None

# Display Info About Grayscale Image
print("\nRead {} As Grayscale".format(args["image"]))
print("Shape: ", img.shape)
print("dytype: ", img.dtype)

# OpenCV Represents Image As NumPy Array.
# RGB Images Loaded In BGR Ordering.
# Shape: (height, width, channels)