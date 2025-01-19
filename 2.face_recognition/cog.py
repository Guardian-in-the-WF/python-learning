import cv2

# 1. 加载 Haar 级联分类器（人脸检测模型）
#   OpenCV 自带了常见的人脸检测 Haar 模型，一般位于 opencv 安装目录下的 data/haarcascades/
#   如果本地没有该文件，需要去 OpenCV GitHub 或官方仓库下载 haarcascade_frontalface_default.xml。
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 2. 打开摄像头
#   如果有多个摄像头，可以把 0 换成 1 或其他索引。
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 3. 循环读取摄像头帧并进行人脸检测
while True:
    ret, frame = cap.read()
    if not ret:
        print("无法读取摄像头画面")
        break

    # 将图像转为灰度，减少计算量并提高检测准确度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测人脸，返回一组 (x,y,w,h)
    # 参数可根据需求调整，如 scaleFactor=1.1, minNeighbors=5, minSize=(30,30) 等
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # 在原图上画矩形标记检测到的人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 显示结果
    cv2.imshow('Face Detection', frame)

    # 若按下 'q' 键，则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. 释放资源，关闭窗口
cap.release()
cv2.destroyAllWindows()
