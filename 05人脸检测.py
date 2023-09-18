# 导入cv模块
import cv2 as cv


def face_detect_demo():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 分类器
    face_detect = cv.CascadeClassifier("D:/software/python/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    # 获得范围
    face = face_detect.detectMultiScale(gray, 1.01, 5, 0, (100, 100), (300, 300))
    for x, y, w, h in face:
        cv.rectangle(img, (x, y, w, h), color=(0, 0, 255), thickness=1)
    cv.imshow("result", img)


# 读取图片
img = cv.imread("text1.jpg")
face_detect_demo()

# 等待(按q退出)
while True:
    if ord("q") == cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()
