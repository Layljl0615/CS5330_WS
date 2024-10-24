# Lab 2: Loading, Displaying, and Saving Images

### Loading Images in OpenCV
#### 1. Loading a Grayscale Image
- Use the `cv2.imread()` function to load an image in grayscale mode.
- Example code:
    ```python
    gray_img = cv2.imread("seal.jpg", cv2.IMREAD_GRAYSCALE)
    ```
- `cv2.IMREAD_GRAYSCALE` specifies that the image will be loaded in grayscale mode.
- If the image cannot be loaded, the function will return an empty matrix (`None`).

#### 2. Loading a Color Image
- Use the `cv2.imread()` function to load an image in color, ignoring transparency.
- Example code:
    ```python
    img = cv2.imread("seal.jpg")
    ```
- This is the default mode, where the image will be loaded in color.
- `cv2.IMREAD_COLOR` is the default flag, which ignores any transparency in the image.

### Displaying Images with OpenCV

#### 1. Displaying an Image in a Window
- Use the `cv2.imshow(window_name, image)` function to display an image in a window.
    ```python
    cv2.imshow("Window Name", img)
    ```
- The `window_name` is the title of the window, and `image` is the image matrix that you want to display.

#### 2. Waiting for a Key Press
- Use `cv2.waitKey()` to wait for a key event or delay the window closure.
    ```python
    cv2.waitKey(0)  # Waits indefinitely until a key is pressed
    ```
- This function takes an argument in milliseconds to specify how long the window should stay open:
    - If `0` is passed, the window will remain open until a key is pressed.
    - If a positive value is passed, the window will close after the specified time (in milliseconds).

#### 3. Closing Windows
- Use `cv2.destroyAllWindows()` to close all the OpenCV windows.
    ```python
    cv2.destroyAllWindows()
    ```
- This function allows you to close all windows at any point in your script after displaying the images.

### Saving Images with OpenCV

#### 1. Saving an Image to a File
- Use the `cv2.imwrite(filename, image)` function to save an image to a file.
    ```python
    cv2.imwrite("output_image.jpg", img)
    ```
- **Parameters**:
    - `filename`: A string representing the name of the file. The file extension must specify the image format (e.g., `.jpg`, `.png`).
    - `image`: The image matrix that you want to save.

#### 2. Supported Image Formats
- The `cv2.imwrite()` function supports various image formats, including:
    - **JPEG**: `.jpg`, `.jpeg`
    - **PNG**: `.png`
    - **TIFF**: `.tiff`, `.tif`
    - **BMP**: `.bmp`
    - **PPM**: `.ppm`
    - **PGM**: `.pgm`

For more information, visit the [geeksforgeeks.org article on `cv2.imwrite()`](https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method/).


