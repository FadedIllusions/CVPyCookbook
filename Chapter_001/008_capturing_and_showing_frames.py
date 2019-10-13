# Import Needed Packages
import cv2


# Init Video Capture Object/Device
capture = cv2.VideoCapture(0)

while True:
	# Read Frame
	_, frame = capture.read()
	
	if not _:
		print("[INFO] Unable To Retrieve Frames From Capture Device...")
		break
	
	# Display Video Steam
	cv2.imshow("Video Stream", frame)
	
	# Define Key Listener
	k = cv2.waitKey(1) & 0xFF
	
	# 'ESC": Exit
	if k == 27:
		break
		
		
# Clean Up
capture.release()
cv2.destroyAllWindows()