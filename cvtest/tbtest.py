import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cv2.namedWindow('Filtered')

cv2.createTrackbar('Filter', 'Filtered', 0, 3, nothing)
cv2.createTrackbar('Kernel', 'Filtered', 1, 20, nothing)
cv2.createTrackbar('Thresh', 'Filtered', 127, 255, nothing)
cv2.createTrackbar('Canny Min', 'Filtered', 50, 255, nothing)
cv2.createTrackbar('Canny Max', 'Filtered', 150, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    filter_type = cv2.getTrackbarPos('Filter', 'Filtered')
    kernel_size = cv2.getTrackbarPos('Kernel', 'Filtered')
    thresh_val = cv2.getTrackbarPos('Thresh', 'Filtered')
    canny_min = cv2.getTrackbarPos('Canny Min', 'Filtered')
    canny_max = cv2.getTrackbarPos('Canny Max', 'Filtered')

    if kernel_size % 2 == 0:
        kernel_size += 1
    if kernel_size < 1:
        kernel_size = 1

    result = frame.copy()

    if filter_type == 1:
        result = cv2.GaussianBlur(result, (kernel_size, kernel_size), 0)
    elif filter_type == 2:
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        _, result = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)
    elif filter_type == 3:
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        result = cv2.Canny(gray, canny_min, canny_max)

    cv2.imshow('Filtered', result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
