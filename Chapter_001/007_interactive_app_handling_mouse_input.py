# Usage:
# python 007_interactive_app_handling_mouse_input.py --image ../data/Lena.png

# Keypressed
# 'c': Crop Image (Make Selection Prior To Keypress)
# 'n': Restore (New) Image
# 'ESC': Exit


# Import Needed Packages
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Input Image")
args = vars(ap.parse_args())


# Read In Image And Copy
image = cv2.imread(args["image"])
image_copy = np.copy(image)


# Define Variables For Mouse Click
# And Starting/Ending Coordinates
mouse_clicked = False
s_x = s_y = e_x = e_y = -1


# Define Mouse Callback Function
def mouse_callback(event, x, y, flags, params):
	global image_copy, s_x, s_y, e_x, e_y, mouse_clicked
	
	# If Left Mouse Button Pushed Down
	if event == cv2.EVENT_LBUTTONDOWN:
		mouse_clicked = True
		s_x, s_y = x, y
		image_copy = np.copy(image)
	# If Mouse Moved
	elif mouse_clicked and event == cv2.EVENT_MOUSEMOVE:
		image_copy = np.copy(image)
		cv2.rectangle(image_copy, (s_x,s_y), (x,y), (0,255,0), 1)
	# If Left Mouse Button Released
	elif mouse_clicked and event == cv2.EVENT_LBUTTONUP:
		mouse_clicked = False
		e_x, e_y = x, y
		
		
# Create Named Window
# Set Mouse Callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)


# Iterate Until 'ESC'
while True:
	# Display Image
	cv2.imshow("Image", image_copy)
	
	# Define Key Listener
	k = cv2.waitKey(1) & 0xFF
	
	# 'c': Crop Image
	if k == ord('c'):
		if s_y > e_y:
			s_y, e_y = e_y, s_y
		if s_x > e_x:
			s_x, e_x = e_x, s_x
		# Crop Image According To Selection	
		if e_y - s_y > 1 and e_x - s_x >0:
			image_copy = image[s_y:e_y, s_x:e_x]
			# We Are Cropping From Original Image
			# So As Not To Show The Selection Rectangle Lines
	
	# 'n': Restore New Image
	elif k == ord('n'):
		image_copy = np.copy(image)
			
	# 'ESC": Quit
	elif k == 27:
		break
		

# Cleanup
cv2.destroyAllWindows()


# Can You Write A Program To Use The Same Concepts
# For An Interactive Zoom In/Out? What About Doing
# So On A Live Stream Once You Learn How To Stream?