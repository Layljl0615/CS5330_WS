# Lab 7: Thresholding
## Thresholding

- A simple way to segment images by turning grayscale image into binary images.

### Simple Thresholding:
- Simple Thresholding: a fixed threshold value is used for the
entire image. Each pixel value is compared to this threshold
value and the pixel is assigned a binary value.
- Pros: easy to implement, works well for uniform lighting.
- Cons: not good for images with varying lighting conditions.

### Adaptive Thresholding:
- Adaptive Thresholding: a threshold value is calculated for
smaller regions of the image rather than the entire image.
- Helpful in cases where lighting conditions vary across an image.
- Two main types of adaptive thresholding:
  - Mean Adaptive Thresholding: threshold is set to be the mean of the
neighborhood values minus a constant
  - Gaussian Adaptive Thresholding: threshold is set as the weighted sum
of the neighborhood values minus a constant
- Pros: handles varying lighting conditions, robust
- Con: slower than simple thresholding
  
### Otsu’s Binarization:
- Otsu’s Binarization: automatically calculates the optimal threshold
value based on the image’s histogram
- Minimizes the variance with the foreground & background pixels to
find the best threshold
- Process:
  - Compute the histogram of the grayscale image
  - Automatically find the optimal threshold value
  - Apply thresholding to binarize the image
- Pros: automatic thresholding, good to use with images with bimodal
histogram
- Cons: doesn’t work well with more complex histograms or uneven
lighting

### Additional information:
- Simple thresholding uses a fixed threshold to convert a grayscale image into a binary image, making it suitable for uniformly lit scenes. However, it performs poorly in images with varying lighting. Adaptive thresholding calculates a threshold based on local regions, making it more effective for handling varying lighting conditions. It comes in two types: Mean Adaptive Thresholding, which uses the average of neighboring pixels, and Gaussian Adaptive Thresholding, which uses a weighted average. Otsu’s binarization automatically calculates the optimal threshold based on the image’s histogram, making it ideal for images with bimodal histograms but less effective for complex or unevenly lit images.
