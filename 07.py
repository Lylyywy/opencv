# 导入cv模块
import cv2 as cv

# 检测函数
def face_detect_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 检测的训练函数位置
    facer = cv.CascadeClassifier("D:/software/python/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    eye = cv.CascadeClassifier('D:/software/python/Lib/site-packages/cv2/data/haarcascade_eye.xml')
    mouth = cv.CascadeClassifier(
        'D:/software/python/Lib/site-packages/cv2/data/haarcascade_mcs_mouth.xml')
    # 对检测进行微调
    faces = facer.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_img = img[y:y + h, x:x + w]

        eyes = eye.detectMultiScale(roi_img, 1.1, 3, 0, (30, 30), (60, 60))
        for (x, y, w, h) in eyes:
            cv.rectangle(roi_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # mouths = mouth.detectMultiScale(roi_img, 1.1, 3, 0, (60, 60), (100, 100))
        # for (x, y, w, h) in mouths:
        #     cv.rectangle(roi_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow("result", img)


# 读取摄像头
cap = cv.VideoCapture(0)
# 循环
while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord("q") == cv.waitKey(1):
        break

# 释放内存
cv.destroyAllWindows()
# 释放摄像头
cap.release()
