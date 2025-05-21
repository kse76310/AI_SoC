import cv2

s1 = cv2.imread('c4.jpg')
s2 = cv2.imread('c5.jpg')
diff = cv2.absdiff(s1,s2)

cv2.imshow("diff",diff)