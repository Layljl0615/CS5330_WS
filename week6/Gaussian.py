import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('../Images/flower.png')

# Apply Gaussian Blur
blurred_gauss = cv2.GaussianBlur(image, (5, 5), 0)  # ksize = (5, 5) and sigmaX = 0

# Convert BGR image (OpenCV default) to RGB for displaying with Matplotlib
blurred_gauss_rgb = cv2.cvtColor(blurred_gauss, cv2.COLOR_BGR2RGB)

# Display the blurred image using Matplotlib
plt.imshow(blurred_gauss_rgb)
plt.title("Gaussian Blurring")
plt.axis('off')  # Hide axis for better visualization
plt.show()
