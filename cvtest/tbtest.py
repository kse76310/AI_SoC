import cv2
import numpy as np

# 콜백 함수 정의 (필수)
def nothing(x):
    pass

title = "Trackbar Blur Test"
image_path = 'c2.jpeg'  # 실제 이미지 파일 경로로 변경해주세요.

# 이미지 불러오기
img_original = cv2.imread(image_path)
if img_original is None:
    print(f"경고: '{image_path}' 파일을 찾을 수 없습니다. 대체 이미지를 사용합니다.")
    img_original = np.zeros((300, 500, 3), dtype=np.uint8)
else:
    # 이미지 복사본을 만들어 원본을 보존합니다.
    img_blurred = img_original.copy()

# 창 생성
cv2.namedWindow(title)

# 첫 번째 트랙바 (임시 - 필요하다면 다른 용도로 활용 가능)
cv2.createTrackbar('Value', title, 0, 255, nothing)

# 두 번째 트랙바 (블러 강도 조절)
cv2.createTrackbar('Blur Level', title, 0, 20, nothing) # 블러 강도는 0부터 20까지 조절

while True:
    # 현재 트랙바 위치 가져오기
    val = cv2.getTrackbarPos('Value', title)
    blur_level = cv2.getTrackbarPos('Blur Level', title)

    img_display = img_original.copy() # 매 프레임마다 원본 이미지를 복사해서 처리

    if blur_level > 0:
        # 블러 강도에 따른 커널 사이즈 계산 (홀수여야 함)
        kernel_size = (blur_level * 2 + 1, blur_level * 2 + 1)
        img_display = cv2.GaussianBlur(img_original, kernel_size, 0)

    # 트랙바 값 화면에 표시 (선택 사항)
    cv2.putText(img_display, f'Value: {val}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img_display, f'Blur: {blur_level}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow(title, img_display)

    # 키 입력 시 종료
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키
        break

cv2.destroyAllWindows()