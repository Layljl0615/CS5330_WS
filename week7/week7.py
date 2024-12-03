import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply simple thresholding
_, thresh_simple = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Apply adaptive mean thresholding
thresh_adaptive_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply adaptive Gaussian thresholding
thresh_adaptive_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Show both results
plt.subplot(1, 2, 1), plt.imshow(thresh_adaptive_mean, cmap='gray')
plt.title('Adaptive Mean Thresholding')

plt.subplot(1, 2, 2), plt.imshow(thresh_adaptive_gaussian, cmap='gray')
plt.title('Adaptive Gaussian Thresholding')

plt.show()

# Show the image
plt.imshow(thresh_simple, cmap='gray')
plt.title('Simple Thresholding')
plt.show()
