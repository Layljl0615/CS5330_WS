# Lab 3: Basics of Images

### Basic Image Operations - Resizing

#### 1. Resizing an Image using `cv2.resize()`
- **Function**: `cv2.resize(image, (width, height), fx, fy, interpolation)`
    - **image**: The input image array (single-channel, 8-bit, or floating-point).
    - **dsize**: The size of the output image array (specified as width and height).
    - **fx**: Scale factor along the horizontal axis (optional).
    - **fy**: Scale factor along the vertical axis (optional).
    - **interpolation**: The interpolation method used for resizing (optional).

#### 2. Common Interpolation Methods:
- **cv2.INTER_LINEAR**: Default interpolation method (bilinear interpolation).
- **cv2.INTER_CUBIC**: Good for enlarging images (slow but produces better quality).
- **cv2.INTER_NEAREST**: Fastest, but may produce lower-quality results.

### Basic Image Operations - Cropping

#### 1. Cropping an Image
- To crop an image, specify the height and width (in pixels) of the area you want to crop:
    ```python
    cropped_img = img[y:y+h, x:x+w]
    ```
- This method uses NumPy array slicing to crop the image.

#### 2. Explanation of Dimensions
- **First dimension**: Refers to the number of rows or the height of the image (vertical axis).
- **Second dimension**: Refers to the number of columns or the width of the image (horizontal axis).

### Basic Image Operations - Rotating

#### 1. Rotating an Image using `cv2.rotate()`
- **Function**: `cv2.rotate(src, rotateCode[, dst])`
    - **src**: The input image.
    - **rotateCode**: An enum to specify how to rotate the image.
    - **dst**: The output image (optional).

#### 2. Common Rotation Codes:
- **To rotate 90 degrees clockwise**:
    ```python
    cv2.ROTATE_90_CLOCKWISE
    ```
- **To rotate 90 degrees counterclockwise**:
    ```python
    cv2.ROTATE_90_COUNTERCLOCKWISE
    ```
- **To rotate 180 degrees**:
    ```python
    cv2.ROTATE_180
    ```
#### 3. Rotating an Image at Custom Angles
If you need to rotate an image by an angle other than 90, 180, or 270 degrees, you can use the following approach:

- **Steps**:
    ```python
    (h, w) = image.shape[:2]  # Get the height and width of the image
    center = (w // 2, h // 2)  # Define the center of rotation
    matrix = cv2.getRotationMatrix2D(center, angle, scale)  # Get the rotation matrix
    rotated_image = cv2.warpAffine(image, matrix, (w, h))  # Apply the affine transformation
    ```

#### 4. Key Parameters:
- **cv2.getRotationMatrix2D()**:
    - Creates the transformation matrix `M` used for rotation.
    - **center**: The center of rotation (usually the center of the image).
    - **angle**: The angle of rotation (positive for anti-clockwise, negative for clockwise).
    - **scale**: The scaling factor, which can resize the image during rotation.

- **cv2.warpAffine()**:
    - Applies the affine transformation, which preserves straight lines and planes during rotation.

### Image Color Spaces and Conversions

#### 1. Default Color Space in OpenCV
- When loading images, OpenCV loads images in **RGB** format by default.

#### 2. Converting Between Color Spaces
- Use `cv2.cvtColor()` to convert an image from one color space to another.

#### 3. Grayscale Color Space
- **Grayscale** is a color space where each pixel represents the intensity of light, ranging from black to white.
- Grayscale images have only one channel instead of three (like RGB).
- **Applications**: Image thresholding, edge detection, object detection, and facial recognition.
    ```python
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ```

#### 4. HSV Color Space
- **HSV** is a cylindrical color space that describes colors using three components:
    - **Hue (H)**: The type of color (0-360°), scaled to 0-179 in OpenCV.
    - **Saturation (S)**: The intensity or purity of the color (0-255).
    - **Value (V)**: The brightness or lightness of the color (0-255).
- **Applications**: Color filtering, object tracking, and image segmentation.
    ```python
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ```

### Drawing Shapes and Text in OpenCV

#### 1. Drawing a Line
- **Function**: `cv2.line(image, (x1, y1), (x2, y2), (color), thickness)`
    - (x1, y1): Starting coordinates.
    - (x2, y2): Ending coordinates.
    - `color`: Color in RGB.
    - `thickness`: Line thickness in pixels.

#### 2. Drawing a Rectangle
- **Function**: `cv2.rectangle(image, (x1, y1), (x2, y2), (color), thickness)`
    - (x1, y1): Top-left corner.
    - (x2, y2): Bottom-right corner.
    - `color`: Color in RGB.
    - `thickness`: Line thickness in pixels.

#### 3. Drawing a Circle
- **Function**: `cv2.circle(image, (center_x, center_y), radius, (color), thickness)`
    - `center_x`, `center_y`: Center coordinates.
    - `radius`: Radius of the circle.
    - `color`: Color in RGB.
    - `thickness`: Line thickness in pixels.

#### 4. Adding Text
- **Function**: `cv2.putText(image, 'text', (x, y), font, fontScale, (color), thickness)`
    - (x, y): Bottom-left corner of the text.
    - `font`: Font type (e.g., `FONT_HERSHEY_SIMPLEX`).
    - `fontScale`: Scale factor for the font.
    - `color`: Text color in RGB.
    - `thickness`: Line thickness in pixels.



