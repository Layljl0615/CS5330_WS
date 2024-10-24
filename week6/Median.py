import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('../Images/flower.png')

# Apply Median Blur
blurred_median = cv2.medianBlur(image, 5)  # ksize = 5, must be an odd number

# Convert BGR image (OpenCV default) to RGB for displaying with Matplotlib
blurred_median_rgb = cv2.cvtColor(blurred_median, cv2.COLOR_BGR2RGB)

# Display the blurred image using Matplotlib
plt.imshow(blurred_median_rgb)
plt.title("Median Blurring")
plt.axis('off')  # Hide axis for better visualization
plt.show()
