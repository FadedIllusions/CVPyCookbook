# Usage:
# python 006_handling_user_keyboard_input.py --image ../data/Lena.png

# Keypresses:
# 'p': Draw Points
# 'l': Draw Line
# 'r': Draw Rectangle
# 'e': Draw Ellipse
# 't': Draw Text


# Import Needed Packages
import numpy as np
import argparse
import random
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Input Image")
args = vars(ap.parse_args())


# Define Finish Variable
finish = False

# Load Image, Copy, Get Width And Height
image = cv2.imread(args["image"])
w, h = image.shape[1], image.shape[0]
image_copy = image.copy()


# Generate Random Point
def rand_pt(mult=1.):
	return (random.randrange(w), random.randrange(h))


# Iterate Until 'Finish'
while not finish:
	# Display Image
	cv2.imshow("reult", image_copy)
	
	# Define Key Listened
	k = cv2.waitKey(1) & 0xFF
	
	# Define Key Events
	# 'p': Draw Points
	if k == ord('p'):
		for pt in [rand_pt() for _ in range(10)]:
			cv2.circle(image_copy, pt, 3, (255,0,0), -1)
	# 'l': Draw Line
	elif k == ord('l'):
		cv2.line(image_copy, rand_pt(), rand_pt(), (0,255,0),3)
	# 'r': Draw Rectangle	
	elif k == ord('r'):
		cv2.rectangle(image_copy, rand_pt(), rand_pt(), (0,0,255), 3)
	# 'e': Draw Ellipse
	elif k == ord('e'):
		cv2.ellipse(image_copy, rand_pt(), rand_pt(), random.randrange(360),
					0, 360, (255,255,0),3)
	# 't': Draw Text	
	elif k == ord('t'):
		cv2.putText(image_copy, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX,
					1, (0,0,0), 3)
	# 'c' Clear Image
	elif k == ord('c'):
		image_copy = np.copy(image)
	# 'ESC': Break Iteration / Exit 	
	elif k == 27:
		finish = True
		
		
# Cleanup
cv2.destroyAllWindows()