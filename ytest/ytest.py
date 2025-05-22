import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5n')

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print('카메라 오픈 에러')
    exit()
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def on_trackbar(val):
    conf_threshold = val / 100
    ret, frame = cam.read()  # 현재 카메라 프레임 읽기
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        return

    results = model(frame)
    result_img = frame.copy()

    for *xyxy, conf, cls in results.xyxy[0]:  # 박스 좌표, confidence, 클래스
        if conf < conf_threshold:
            continue  # 기준 미달이면 건너뜀
        x1, y1, x2, y2 = map(int, xyxy)
        label = f"{model.names[int(cls)]} {conf:.2f}"
        cv2.rectangle(result_img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(result_img, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Detection', result_img)

cv2.namedWindow('Detection')
cv2.createTrackbar('Confidence', 'Detection', 25, 100, on_trackbar)

on_trackbar(25) # 초기 트랙바 값으로 한번 실행

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()