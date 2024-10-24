import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('../Images/flower.png')

# Apply Bilateral Filter
blurred_bilateral = cv2.bilateralFilter(image, 9, 75, 75)  # d = 9, sigmaColor = 75, sigmaSpace = 75

# Convert BGR image (OpenCV default) to RGB for displaying with Matplotlib
blurred_bilateral_rgb = cv2.cvtColor(blurred_bilateral, cv2.COLOR_BGR2RGB)

# Display the blurred image using Matplotlib
plt.imshow(blurred_bilateral_rgb)
plt.title("Bilateral Filtering")
plt.axis('off')  # Hide axis for better visualization
plt.show()
