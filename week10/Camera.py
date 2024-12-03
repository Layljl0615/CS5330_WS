import cv2

# Set up camera
cap = cv2.VideoCapture(0)

# Parameters for Shi-Tomasi Corner Detection to find points for Lucas-Kanade
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# Parameters for Lucas-Kanade Optical Flow
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Read the first frame
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Detect initial points to track using Shi-Tomasi Corner Detection
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
