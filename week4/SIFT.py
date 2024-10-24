import cv2
import numpy as np

# Part 1: Loading Images
image = cv2.imread('../Images/flower.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# SIFT Detector
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw keypoints
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None,
                                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show the image with detected keypoints
cv2.imshow('SIFT Keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
