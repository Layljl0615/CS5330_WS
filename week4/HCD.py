import cv2
import numpy as np

# Part I: Loading Images
image = cv2.imread('../Images/flower.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Harris Corner Detection
gray = np.float32(gray)
harris_corners = cv2.cornerHarris(gray, blockSize=20, ksize=3, k=0.04)

# Dilate the detected corners to enhance them
harris_corners = cv2.dilate(harris_corners, kernel=None)

# Threshold for an optimal value
image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

# Show the image with detected corners
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
