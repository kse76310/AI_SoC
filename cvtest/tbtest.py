import cv2

# 콜백 함수 정의 (필수)
def nothing(x):
    pass

title = "Trackbar test"

# 창 생성
cv2.namedWindow(title)

# 트랙바 생성
cv2.createTrackbar('name1', title, 0, 255, nothing)

# 트랙바 값 확인 루프 (선택사항)
while True:
    # 현재 트랙바 위치 가져오기
    val = cv2.getTrackbarPos('name1', title)
    
    # 아무 내용 없는 빈 창 보여주기
    img = cv2.imread('some_image.jpg')  # 혹은 np.zeros((100, 300, 3), dtype=np.uint8)
    if img is None:
        img = cv2.cvtColor(cv2.UMat(300, 500, cv2.CV_8UC3), cv2.COLOR_BGR2RGB)  # 대체용 빈 이미지

    cv2.putText(img, f'Value: {val}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.imshow(title, img)

    # 키 입력 시 종료
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키
        break

cv2.destroyAllWindows()
