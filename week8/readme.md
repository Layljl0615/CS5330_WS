# Lab 8: Edge Detection
- Edge detection: process of identifying and locating sharp discontinuities in
an image – these reflect significant alterations in pixel intensity, which often
correspond to object boundaries
- Application of edge detection
  - Object recognition
  - Image segmentation
  - Pattern recognition

### Sobel Edge Detection (Sobel Operator)
- Sobel Operator: uses a pair of convolution kernels to calculate the
gradient in horizontal and vertical directions.
- Highlights changes in intensity, providing both direction and
magnitude of the edges.
- Why use Sobel?
  - Efficient: Sobel is computationally efficient and is good for detecting
edges in simple images.
  - Edge Direction: It provides information not only about where the edges
are but also about their orientation (horizontal, vertical, or diagonal).
### Canny Edge Detection
- Canny Edge Detection: multi-step algorithm to detect a wide
range of edges in images.
- More refined than Sobel and commonly used in practice.
- Steps involved: Noise reduction, gradient calculation, non-
maximum suppression, double threshold, edge tracking by
hysteresis.
- Why use canny?
  - Accuracy: Canny is very precise in detecting edges and reducing noise.
  - Multi-step Process: Each step (smoothing, gradient, non-maximum
suppression, thresholding) refines the edge detection process, leading to
more robust results.
### Additional information:
Edge detection helps in identifying object boundaries by detecting sharp intensity changes in images. Sobel edge detection is fast and works well for simple images, detecting edges in horizontal and vertical directions. It’s computationally efficient but doesn’t handle noise well. Canny edge detection, on the other hand, is more advanced, involving multiple steps like noise reduction and gradient calculation, to provide more accurate and noise-resistant results, making it suitable for complex images. Canny’s multi-step approach makes it a more robust choice for edge detection tasks in real-world applications.
