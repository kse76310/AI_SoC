import cv2

print(cv2.__version__)

print(cv2.getBuildInformation())

gst = "gst-launch-1.0 v4l2src device=/dev/video0 ! \video/x-raw,width=640,height=480,framerate=30/1 ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! udpsink host=127.0.0.1 port=5000"

cap = cv2.VideoCapture(gst, cv2.CAP_GSTREAMER)

if cap.isOpened():
    print("")