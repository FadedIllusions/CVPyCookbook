# Usage:
# python 009_playing_stream_from_video.py --video ../data/drop.avi


# Import Needed Packages
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path To Video File")
args = vars(ap.parse_args())


# Init Video Capture Device
capture = cv2.VideoCapture(args["video"])


while True:
	# Grab Frame
	_, frame = capture.read()
	
	# If No Frames Read
	if not _:
		print("[INFO] Video Cannot Be Read...")
		break
		
	# Display Frame
	cv2.imshow("Video", frame)
	
	# Define Key Listener
	k = cv2.waitKey(1) & 0xFF
	
	# 'ESC': Exit
	if k == 27:
		break
		
		
# Cleanup
capture.release()
cv2.destroyAllWindows()