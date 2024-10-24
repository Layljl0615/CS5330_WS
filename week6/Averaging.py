import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('../Images/flower.png')

# Apply Averaging (Box Filter)
blurred_avg = cv2.blur(image, (5, 5))  # ksize = (5, 5) for averaging

# Convert BGR image (OpenCV default) to RGB for displaying with Matplotlib
blurred_avg_rgb = cv2.cvtColor(blurred_avg, cv2.COLOR_BGR2RGB)

# Display the blurred image using Matplotlib
plt.imshow(blurred_avg_rgb)
plt.title("Averaging (Box Filter)")
plt.axis('off')  # Hide axis for better visualization
plt.show()
