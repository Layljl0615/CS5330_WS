import cv2 # Load and preprocess the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (128, 128)) / 255.0  # Normalize to range [0, 1]

# Add Gaussian noise in steps
for i in range(5):  # 5 noise addition steps
    noise = np.random.normal(0, 0.1 * (i + 1), image.shape)  # Increase noise level
    noisy_image = np.clip(image + noise, 0, 1)  # Ensure values are within [0, 1]
    cv2.imshow(f"Step {i+1}", (noisy_image * 255).astype('uint8'))  # Show noisy image
    cv2.waitKey(0)  # Wait for user input to close the windows

# Denoising using GaussianBlur
denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)

cv2.imshow("Denoised Image", (denoised_image * 255).astype('uint8'))
cv2.waitKey(0)
