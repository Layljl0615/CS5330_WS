# Histogram

## Introduction to Histograms

### 1. What is a Histogram?
- A **histogram** is a graphical representation showing the frequency of pixel intensity values in an image.
- **Pixel Intensity**: Ranges from 0 (black) to 255 (white) for grayscale images.
- **Usage of Histograms**: Helps understand pixel distribution in an image, useful for tasks like image thresholding, contrast adjustment, and object detection.

### 2. Types of Histograms
- **Grayscale Histogram**: Plots the intensity values of pixels in a grayscale image.
  - **X-axis**: Represents pixel intensity values (0-255).
  - **Y-axis**: Represents the number of pixels at each intensity level.
  - **Usages**: Brightness and contrast analysis, image equalization, thresholding, object detection, etc.
  
- **Color Histogram**: Separate histograms for each of the three color channels (Red, Green, Blue).
  - **Usages**: Image classification, color enhancement, dominant color extraction, object recognition, etc.

---

## Grayscale Histogram Implementation

### 1. Calculating the Histogram
To calculate and plot a histogram in OpenCV for a grayscale image:

```python
import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('image.jpg', 0)

# Calculate the histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(hist)
plt.show()
```
## Color Histogram Implementation

### 1. Calculating the Histogram for Color Images

- **`cv2.calcHist()`**: This OpenCV function computes the histogram of an image.

#### Code Example:
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in color mode
img = cv2.imread('image.jpg')

# Calculate the histogram for each color channel
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    
# Display the histograms
plt.show()
```
