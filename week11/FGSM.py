import cv2
import numpy as np

# Load original image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Create noise
noise = np.random.normal(0, 25, image.shape).astype('uint8')

# Add noise to create adversarial image
adversarial_image = cv2.addWeighted(image, 1.0, noise, 0.1, 0)

cv2.imshow('Adversarial Image', adversarial_image)
cv2.waitKey(0)
