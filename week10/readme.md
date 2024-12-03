# Lab 10: Camera

### Setting up Camera in OpenCV
- Cv2.VideoCapture(0)
  - 0 is used for default camera
  - 1 is used for external camera, if available
- Reading and Displaying Frames
  - After accessing the camera, we can read frames in a loop and display them
  - Common functions that are utilized:
    - cap.read() -> caputres each frame the camera
    - cv2.imshow(“Camera Feed”, frame) -> displays the current frame
    - Note: att the end, you need to release the camera using cap.release()

### Introduction to Optical Flow
- Optical Flow: tracks the apparent motion of pixels between
consecutive frames.
  - Detects changes over time, making it useful for tracking objects or
identifying movements of an object
- In this lab, we will learn how we can implement optical flow for:
  - Motion detection
  - Feature tracking

### Motion Detection using Optical Flow
- There are two methods when using optical flow to detect motions
  - Lucas-Kanade Optical Flow
    - Commonly used method for sparse optical flow
    - Tracks specified feature points across frames
    - Strengths: computationally efficient, accurate for tracking feature points, less
    sensitive to small motions, scalable
    - Weaknesses: not suitable for large motions, limited to specific points
  - Dense Optical Flow
    - Calculates optical flow for all points in the frame, which can be computationally
    intensive
    - Strengths: detailed motion information, good for large motions, useful for scene-
    wide analysis
    - Weaknesses: computationally intensive, slower processing, sensitive to noise
  
### Motion Detection using Optical Flow
- Lucas-Kanade Optical Flow (Sparse)
  - cv2.calcOpticalFlowPyrLK(prev_frame, next_frame, prev_points, None,
  **params)
    - prev_frame: The first frame (grayscale) in which the initial points are located. It
    serves as the starting point for tracking.
    - next_frame: The subsequent frame (also in grayscale) where the algorithm will
    search for the new position of the points.
    - prev_points: The points in prev_frame that you want to track in next_frame. Typically
    detected using cv2.goodFeaturesToTrack.
    - None: Placeholder for output array, which we set to None.
    - params: A dictionary containing parameters for the Lucas-Kanade method.
      
### Motion Detection using Optical Flow
- Dense Optical Flow
  - cv2.calcOpticalFlowFarneback(prev_frame, next_frame, None, pyr_scale, levels,
  winsize, iterations, poly_n, poly_sigma, flags)
    - prev_frame: The first frame (grayscale) in which motion is calculated.
    - next_frame: The subsequent frame (also grayscale) where the optical flow is calculated.
    - None: Placeholder for the output array, which we set to None in typical usage.
    - pyr_scale: Parameter specifying the image scale between pyramid levels (0 to 1). For example, 0.5
    scales the image to half its size at each level. A smaller scale increases accuracy but requires more
    computation.
    - levels: Number of pyramid levels used in the calculation. More levels improve the algorithm's
    ability to track large motions but increase computation.
    - winsize: Size of the window used for averaging flow. A larger window smooths the flow but may lose
    finer details.
    - iterations: Number of iterations the algorithm does at each pyramid level to refine the flow.
    - poly_n: Size of the pixel neighborhood used to find polynomial expansion in each pixel. Larger
    values are more robust to noise but require more computation. Common values are 5 or 7.
    - poly_sigma: Standard deviation of the Gaussian used for neighborhood weighting. A larger value
    results in smoother flow but reduces sensitivity to smaller motion.
    - flags: Operation flags for modifying the algorithm behavior.



### Additional information:
To set up a camera in OpenCV, you can use cv2.VideoCapture(0) for the default camera or cv2.VideoCapture(1) for an external camera. Once the camera is accessed, frames can be captured in a loop using cap.read() and displayed using cv2.imshow("Camera Feed", frame). After finishing, remember to release the camera with cap.release().

Optical Flow tracks the apparent motion of pixels between consecutive frames, helping to detect changes over time. It's useful for applications like motion detection and feature tracking, allowing us to monitor the movement of objects across video frames.
