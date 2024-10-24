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

# Displaying the cropped image
cv2.imshow("cropped", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
