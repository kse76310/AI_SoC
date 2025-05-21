import cv2

img = cv2.imread('c1.jpg')
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2BGR565)

cv2.imshow("",img)
cv2.imshow("Converted",gimg)
cv2.waitKey(0)
