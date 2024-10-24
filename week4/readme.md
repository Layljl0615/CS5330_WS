# Lab 4: Image Processing
## Introduction to Feature Detection and Matching

### 1. Feature Detection
- **Features**: Specific structures or patterns in an image that are easily distinguishable.
- **Examples of Features**: Edges, corners, and blobs.

### 2. Keypoint Detection
- **Keypoints**: Distinct points in an image that are invariant to transformations such as scaling and rotation.
- **Methods for Keypoint Detection**:
  - **Harris Corner Detector**
  - **SIFT (Scale-Invariant Feature Transform)**

### 3. Harris Corner Detector
- **Description**: A corner detection operator used to extract corners and detect features in an image by considering the differential of corner scores in various directions.

### 4. SIFT (Scale-Invariant Feature Transform)
- **Description**: An algorithm used to detect, describe, and match local features in images.
- **Object Recognition**: SIFT recognizes objects in new images by comparing features from the new image to a database of known features. Matching features are found based on the Euclidean distance between their feature vectors.

### 5. Feature Invariance
- Ensures that keypoints remain consistent under different conditions such
as scale, rotation, and illumination changes.
- Vital for creating robust image processing systems.

## Implementing Keypoint Detection - Harris Corner Detector (HCD)

### 1. `cv2.cornerHarris()`
The function `cv2.cornerHarris()` is used to detect corners in an image using the Harris Corner Detection method.

#### Parameters:
- **src**: The input image (should be converted to grayscale).
- **dest**: The output image where the Harris detector responses will be stored.
- **blockSize**: The size of the neighborhood considered for corner detection.
- **kSize**: Aperture parameter for the Sobel() operator, which is used for calculating image derivatives.
- **freeParameter (k)**: The Harris detector free parameter, usually a value between 0.04 and 0.06.
- **borderType**: The method used to extrapolate pixels at the border of the image.

### 2. `cv2.dilate()`
- Dilates an image by using a specific structuring element that determines
the shape of a pixel neighborhood which the maximum is taken
  
## Implementing Keypoint Detection - SIFT (Scale-Invariant Feature Transform)

### 1. Creating a SIFT Object
- **Function**: `sift = cv2.SIFT_create()`
- **Usage**: Used to create a SIFT object for keypoint detection and descriptor extraction.

### 2. Detecting Keypoints and Computing Descriptors
- **Function**: `sift.detectAndCompute()`
- **Usage**: Detects keypoints and computes descriptors for each keypoint in an image.

### 3. Drawing Keypoints on the Image
- **Function**: `cv2.drawKeypoints()`
- **Usage**: Draws the detected keypoints on an image for visualization.

## Feature Matching with FLANN

### 1. What is FLANN?
- **FLANN (Fast Library for Approximate Nearest Neighbors)** is an algorithm used to match feature descriptors between images.
- It contains a collection of algorithms optimized for **nearest neighbor search** and includes a system for automatically selecting the best algorithm and optimum parameters based on the dataset.
- FLANN is written in C++ and has bindings for C, MATLAB, Python, and Ruby.

### 2. FLANN Parameters
- **FLANN_INDEX_KDTREE**: This algorithm uses KD-tree for indexing, which efficiently organizes points in space, useful for nearest neighbor searches.
  
#### Parameters:
- **algorithm**: Specifies the algorithm for indexing. In this case, `FLANN_INDEX_KDTREE` is used.
- **trees**: Defines the number of trees in the KD-tree. More trees may result in a more accurate but slower search.

### 3. `index_params` Dictionary
- The `index_params` dictionary defines how the feature descriptors will be indexed.

#### Parameters:
- **algorithm**: Specifies the algorithm to use for indexing (e.g., `FLANN_INDEX_KDTREE`).
- **trees**: Specifies the number of trees to be used in the KD-tree.

### 4. `search_params` Dictionary
- The `search_params` dictionary controls the search behavior during nearest neighbor matching.

#### Parameters:
- **checks**: Specifies the number of times the tree(s) will be recursively traversed. A higher value results in a more exhaustive search, potentially increasing accuracy at the cost of speed (default is usually around 50).

### 5. FLANN Matching with `flann.knnMatch()`
- **Function**: `knnMatch()` performs K-Nearest Neighbor matching between the descriptors of two images, returning the k best matches for each descriptor.

#### Parameters:
- **descriptors1**: The descriptors from the first image.
- **descriptors2**: The descriptors from the second image.
- **k**: The number of nearest neighbors to find for each descriptor.
