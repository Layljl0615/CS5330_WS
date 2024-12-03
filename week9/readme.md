# Lab 9: Contours
- Contours: closed curves that follow the continuous boundary points of an
object within an image. Captures the shape and outline of objects, making
them useful for object segmentation and shape analysis.
- Application of edge detection
  - Object detection
  - Object segmentation
  - Object recognition
  - Shape analysis


- Usual steps in detecting contours
- Convert image to a binary image by converting it to grayscale and applying
thresholding
- Why? Because this will simplify the distinction between the object and the
background, making it easier to detect boundaries
  - Retrieve & approximate contours
  - There are various ”modes” when it comes to retrieving or approximating contours,
  which we will delve more in the following slides
  - Draw the approximated contours

- Different modes for contour retrieval include:
- RETR_EXTERNAL: Retrieves only the outermost contours, ignoring any nested
contours. Useful for detecting the overall shape of objects.
- RETR_LIST: Retrieves all contours without establishing a hierarchical
relationship. This mode returns all contours as a flat list.
- RETR_TREE: Retrieves all contours and organizes them in a hierarchical
structure, showing the relationships between nested contours (e.g., an object
within another object)

- cv2.drawContours(image, contours, contourIdx, color, thickness)
  - image: The image where contours will be drawn.
  - contours: List of contours obtained from findContours.
  - contourIdx: Index of the contour to draw. Use -1 to draw all contours.
  - color: Color of the contour lines (e.g., (0, 255, 0) for green).
  - thickness: Thickness of the contour lines.


### Additional information:
Contours are closed curves that trace the continuous boundary of objects in an image, making them useful for tasks such as object detection, segmentation, and shape analysis. To detect contours, an image is first converted to binary by grayscale conversion and thresholding, simplifying the distinction between objects and the background. Different contour retrieval modes—RETR_EXTERNAL (for outer contours), RETR_LIST (for all contours without hierarchy), and RETR_TREE (for hierarchical contours)—allow for different levels of detail. Contours can be drawn using cv2.drawContours, where you can specify the color, thickness, and which contours to display.

