# Usage:
# python 005_drawing_2d_primatives.py --image ../data/Lena.png


# Import Needed Packages
import argparse
import random
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Input Image")
args = vars(ap.parse_args())


# Load Image, Get Width And Height
image = cv2.imread(args["image"])
w, h = image.shape[1], image.shape[0]

# Display Original Image
cv2.imshow("Original", image)


# Generate Random Point (As Float)
# Passing In Multiplier, Defaulting To Identity
def rand_pt(mult=1.):
	return (random.randrange(int(w*mult)), 
			random.randrange(int(h*mult)))

# Draw Primatives -- Circles, Lines, Rectangles, Etc
# From And To Random Points In Image
# LINE_AA Gives Us An Alias-Free Border
cv2.circle(image, rand_pt(), 40, (255,0,0))
cv2.circle(image, rand_pt(), 40, (255,85,85), 2)
cv2.circle(image, rand_pt(), 5, (255,0,0), cv2.FILLED)
cv2.circle(image, rand_pt(), 40, (255,170,170), 2, cv2.LINE_AA)
cv2.line(image, rand_pt(), rand_pt(), (0,255,0))
cv2.line(image, rand_pt(), rand_pt(), (85,255,85), 3)
cv2.line(image, rand_pt(), rand_pt(), (170,255,170), 3, cv2.LINE_AA)
cv2.arrowedLine(image, rand_pt(), rand_pt(), (0,0,255), 3, cv2.LINE_AA)
cv2.rectangle(image, rand_pt(), rand_pt(), (255,255,0),3)
cv2.ellipse(image, rand_pt(), rand_pt(0.3), random.randrange(360), 0, 360, (255,255,255), 3)
cv2.putText(image, "OpenCV", rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)


# Display Created Image
cv2.imshow("Result", image)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()