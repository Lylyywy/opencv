import os
import cv2
import numpy as np
from PIL import Image


def getImageAndLabels(path):
    # 存储人脸数据和姓名数据
    facesSamples = []
    ids = []
    # 存储图片信息
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # 加载分类项
    face_detector = cv2.CascadeClassifier(
        "D:/software/python/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    # 遍历列表中的图片
    for imagePath in imagePaths:
        # 打开图片，灰度化，PIL有九种模式:1(黑白), L（灰度）, P, RGB, RGBA, CMYK, YCbCr, I, F
        PIL_img = Image.open(imagePath).convert("L")
        # 以黑白深浅将图片转换为数组
        img_numpy = np.array(PIL_img, "uint8")
        # 获取图片人脸特征
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图片的id和姓名
        id = os.path.split(imagePath)[1].split(".")[1]
        # 获取脸的数据
        for x, y, w, h, in faces:
            ids.append(id)
            facesSamples.append(img_numpy[x:x + w, y:y + h])
        # 打印脸部特征和ID
        print("id:", id)
        print("fs:", facesSamples)
        facesSamples = []
    return facesSamples, ids


if __name__ == "__main__":
    # 图片路径
    path = "./date/jm/"
    # 获取图像数组与ID数组
    faces, ids = getImageAndLabels(path)
    # 加载识别器
    #recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 训练
    #recognizer.train(faces, np.array(ids))
    # 保存文件
    #recognizer.write("trainer/trainer.yml")
