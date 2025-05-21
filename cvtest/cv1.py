import cv2

s_img = cv2.imread('c1.jpg')
##c_img = cv2.GaussianBlur(s_img,(7,7),0)
#c_img = cv2.threshold(s_img,(7,7),0)
#gimg = cv2.cvtColor(img,cv2.COLOR_BGR2BGR565)
c_img = cv2.Canny(s_img,100,200)

cv2.imshow("",s_img)
cv2.imshow("Converted",c_img)
cv2.waitKey(0)
