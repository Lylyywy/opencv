# 导入cv模块
import cv2 as cv


def face_detect_demo():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 检测的训练函数位置
    face_detect = cv.CascadeClassifier(
        "D:/software/python/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    # 对检测进行微调
    # face = face_detect.detectMultiScale(gray, 1.05, 5, 0, (10, 10), (100, 100))
    face = face_detect.detectMultiScale(gray)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y, w, h), color=(0, 0, 255), thickness=1)
    cv.imshow("result", img)
    cv.imwrite("result1_text1.jpg", img)


# 读取图片
img = cv.imread("text2.jpg")
face_detect_demo()

# 等待(按q退出)
while True:
    if ord("q") == cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()
