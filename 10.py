import cv2
import os
import urllib
import urllib.request


recogizer = cv2.face.LBPHFaceRecognizer_create()
#加载训练数据集
recogizer.read("trainer/trainer.yml")

names = []

warningtime = 0

def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

statusStr = {
    "0":"短信发送成功",
    "-1":"参数不全",
    "-2":"服务器空间不支持",
    "30":"密码错误",
    "40":"账号不存在",
    "41":"余额不足",
    "42":"账户已过期",
    "43":"IP地址限制",
    "50":"内容含有敏感词"
}

def warning():
    smsapi = "http://api.smsbao.com/"
    user = "185****0183"
    password = md5("*******")
    content = "[报警]\n原因：xxx\n地点：xxx\n时间：xx"
    phone = "185****0183"

    data = urllib.parse.urlencode({"u":user, "p":password, "m":phone, "c":content})
    send_url = smsapi + "sms?" + data
    respose = urllib.request.urlopen(send_url)
    the_page = respose.read().decode("utf-8")
    print(statusStr[the_page])

def face_detect_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier("D:/software/python/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    face = face_detect.detectMultiScale(gray, 1.1, 5, 0, (100, 100), (600, 600))
    for x, y, w, h in face:
        cv.rectangle(img, (x, y, x+w, y+h), color=(0, 0, 255), thickness=2)
        cv.circle(img, center=(x + w//2, y + h//2), radius=w//2, color=(0, 255, 0), thickness=1)
        #人脸识别
        ids, cofidence = recognizer.predict(gray[y:y+h, x:x+w])

        if cofidence > 80:
            global warningtime
            warningtime += 1
            if warningtime > 100:
                warning()
                warningtime = 0
            cv2.putText(img, "unkonw", (x+10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 1)
        else:
            #cv2.putText(img, str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.putText(img, str("ly"), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv.imshow("result", img)

#def name():


cap = cv.VideoCapture(0)
#循环
while True:
    flag,frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord("q") == cv.waitKey(1):
        break

#释放内存
cv.destroyAllWindows()
#释放摄像头
cap.release()