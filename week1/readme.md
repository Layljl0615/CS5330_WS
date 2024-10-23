Importing CV2 on PyCharm：
* Click on ”Files” on the top-right corner of your screen
* Click on “Settings” and then to Project: “Name of Your Project”
* Click on “Python Interpreter” (On Mac, you can find “Settings”
under the “PyCharm” Menu)
* Then expand on the box that’s next to “Python Interpreter: “ and
click “Show All”
* Click on Python 3.10 so it is highlighted then click “OK”
* Click on the “+” sign that is right above “Package”
* Search “opencv-python” and then install the package

Setting up OpenCV in Visual Studio Code
* On the new terminal
* On your terminal run the following commands:
* python –m venv myvenv
* .\myvenv\Scripts\activate
* pip install opencv-python
Info from:
https://www.youtube.com/watch?v=ZQcIFCBeSgM&ab_channel=TheCodeCity

Setting up OpenCV in Command Line
* Terminal on Mac (or cmd.exe in Windows)
* Create Virtual Environment
* Install OpenCV
$ pip3 install opencv-python
* Test
$ python3 -c "import cv2; print(cv2.__version__)"

