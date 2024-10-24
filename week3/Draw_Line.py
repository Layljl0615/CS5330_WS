import cv2
import numpy as np

# Part I: Loading Images

# This loads the image in color (the original format)
img = cv2.imread("../Images/flower.png")

# This loads the image in grayscale
gray_img = cv2.imread("../Images/flower.png", cv2.IMREAD_GRAYSCALE)

# Resizing an image
resized_img = cv2.resize(img, dsize=(500, 500))

# Cropping an image
cropped_img = img[80:280, 150:330]

# Rotating the cropped image
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Drawing a line on the image (with coordinates within the image size)
line_img = cv2.line(img, pt1=(50, 50), pt2=(400, 400), color=(0, 0, 0), thickness=5)

# Displaying the image with the line
cv2.imshow("line image", line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
