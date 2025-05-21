import cv2

s1 = cv2.imread('c4.jpg')
s2 = cv2.imread('c5.jpg')
diff = cv2.absdiff(s1,s2)
r,thre = cv2.threshold(diff, 120, 255, cv2.THRESH_BINARY)
cann = cv2.Canny(diff,100,200)

#cv2.imshow('s1',s1)
#cv2.imshow('s2',s2)

cv2.imshow("diff",diff)
cv2.imshow("threshold",thre)
cv2.imshow("Canny",cann)



cv2.waitKey()