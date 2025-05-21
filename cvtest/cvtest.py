import cv2
import time
cam = cv2.VideoCapture(0)

if not cam.isOpened():
	print('카메라 오픈 에러')
	exit()
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(1)!=27:
	ret,f = cam.read()
	cv2.imshow('aa',f)
cv2.imwrite('c1.jpg',f)
cv2.waitKey()
cv2.destroyAllWindows()
