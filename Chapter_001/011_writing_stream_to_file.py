# Import Needed Packages
import cv2


# Init Video Capture Device
capture = cv2.VideoCapture(0)

# Get Frame Width And Height
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Frame Width: ", frame_width)
print("Frame Height: ", frame_height)

# Define Video Writer
# (output_file, codec, fps, width, height)
output = cv2.VideoWriter("../data/001Video.avi", cv2.VideoWriter_fourcc(*'XVID'),
						 25, (frame_width, frame_height))


while True:
	# Get Frame
	_, frame = capture.read()
	
	# If Unable To Get Frame
	if not _:
		print("[INFO] Unable To Access Capture Device...")
		break
		
	# Write Video To File
	output.write(frame)
	
	# Display Frame Stream
	cv2.imshow("Video Stream", frame)
	
	# Define Key Listener
	# 'ESC': Exit
	k = cv2.waitKey(1) & 0xFF
	if k ==27:
		print("[INFO] \'ESC\' Pressed...")
		break
		
		
# Cleanup
capture.release()
output.release()
cv2.destroyAllWindows()