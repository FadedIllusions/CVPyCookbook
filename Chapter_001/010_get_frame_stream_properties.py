# Import Needed Packages
import cv2


def print_capture_properties(*args):
	# Init Video Capture Device
	capture = cv2.VideoCapture(*args)
	
	# Print Frame Properties
	print("\n--- --- ---### Capture Properties ###--- --- ---")
	print("Created Capture: ", " ".join(map(str, args)))
	print("Frame Count: ", int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
	print("Frame Width: ", int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
	print("Frame Height: ", int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	print("Frame Rate: ", capture.get(cv2.CAP_PROP_FPS))
	print("\n")

	# Cleanup
	capture.release()

print_capture_properties("../data/drop.avi")
print_capture_properties(0)

