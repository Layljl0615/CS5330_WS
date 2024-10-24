import cv2
import os

# Part I: Loading Images

# Load the image in color
img = cv2.imread("../Images/flower.png")

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not loaded correctly.")
else:
    print("Image loaded successfully.")

# Get the current working directory
print("Current working directory:", os.getcwd())

# Saving image
if cv2.imwrite("lab_2_image.jpg", img):
    print("Image saved successfully.")
else:
    print("Failed to save image.")

# Displaying images
cv2.imshow("flower.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
