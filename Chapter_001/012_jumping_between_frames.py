# Positioning VideoCapture Objects At Different Frame Positions

# Import Needed Packages
import cv2


# Init Video Capture Object, Read In File
capture = cv2.VideoCapture("../data/drop.avi")
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

# Get Frame Count
# Print Frame Property Elements
print("Frame Count: ", frame_count)
print("Position: ", int(capture.get(cv2.CAP_PROP_POS_FRAMES)))

# Get And Display First Frame
_, frame = capture.read()
cv2.imshow("frame0", frame)
cv2.waitKey(0)

# Get New Frame Position, Grab And Display
print("Position: ", int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow("frame1", frame)
cv2.waitKey(0)

# Set Frame Position, Print To Confirm
# Get And Display Frame
capture.set(cv2.CAP_PROP_POS_FRAMES, 100)
print("Position: ", int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow("frame100", frame)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()