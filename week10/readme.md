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


### Additional information:
To set up a camera in OpenCV, you can use cv2.VideoCapture(0) for the default camera or cv2.VideoCapture(1) for an external camera. Once the camera is accessed, frames can be captured in a loop using cap.read() and displayed using cv2.imshow("Camera Feed", frame). After finishing, remember to release the camera with cap.release().

Optical Flow tracks the apparent motion of pixels between consecutive frames, helping to detect changes over time. It's useful for applications like motion detection and feature tracking, allowing us to monitor the movement of objects across video frames.
