import cv2


video_capture = cv2.VideoCapture(0)  # 将视频源设置成默认的摄像头
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")  # 此文件是opencv的haar人脸特征分类器
face_cascade.load('.\haarcascade_frontalface_alt2.xml')  # 一定要告诉编译器文件所在的具体位置

while True:
    ret, frame = video_capture.read()  # 读取该视频
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将图片转化成灰度
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)   # 检测脸部
    num = 0   # 脸部数量
    for (x, y, w, h) in faces:
        num += 1
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按“q”退出
        break
video_capture.release()
cv2.destroyAllWindows()
if num > 2:
    print('N')
else:
    print(num)




