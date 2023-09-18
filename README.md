中文简体|[English](./README.en.md)

<div align="center">
	<a href="https://gitee.com/gitlystudy/opencv.git">
	<img src="https://foruda.gitee.com/avatar/1690360352320899582/11079075_luo_yong_gitee_1690360352.png!avatar100" alt="Simple Icons" >
	</a>
<p align="center">
    基于OpenCV的python程序，适用于计算机视觉数据采集，实时视频帧收集等。
</p>
</div>

## 作者简介
罗岩, 一位平平无奇的代码爱好者；

Github: https://github.com/Lylyywy/opencv.git


<h2 align="center">项目使用</h2>

### 01读取图像
```shell
cv.imread("text.jpg")
```
<div align="center" >
<img src="https://pic.imgdb.cn/item/6507f1cc204c2e34d38f4f7c.jpg">
</div>

### 02颜色转换
```shell
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
```
<div align="center" >
<img src="https://pic.imgdb.cn/item/6507f2ed204c2e34d38f9886.jpg">
</div>

```shell
bgr_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
```
<div align="center" >
<img src="https://pic.imgdb.cn/item/6507f30d204c2e34d38f9f4b.jpg">
</div>

```shell
hsv_img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
```
<div align="center" >
<img src="https://pic.imgdb.cn/item/6507f323204c2e34d38fa417.jpg">
</div>

```shell
ycrcb_img = cv.cvtColor(img, cv.COLOR_RGB2YCrCb)
```
<div align="center" >
<img src="https://pic.imgdb.cn/item/6507f335204c2e34d38fa887.jpg">
</div>

### 03尺寸修改
```shell
img = cv.imread("text21.jpg")
h, w = img.shape[:2]

resize_img = cv.resize(img, dsize=(200, 200))       #修改尺寸大小为（200,200）
resize_img1 = cv.resize(img, dsize=(w//4, h//4))    #修改尺寸为原大小的四分之一
```
### 04绘制矩形框
```shell
# 坐标(x:起点到图像最左边的距离，y:起点到图像上边距离，w:起点向右走的距离，h:起点向下走的距离，r:圆的半径)
x, y, w, h = 100, 200, 10, 100
# 绘制
cv.rectangle(img, (x, y, w, h), color=(0, 0, 255), thickness=1)
cv.circle(img, center=(x, y), radius=100, color=(0, 255, 0), thickness=2)
```
<div align="center" >
<img src="https://pic.imgdb.cn/item/6507f582204c2e34d390753e.jpg">
</div>

### 05人脸位置检测
```shell
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 分类器
    face_detect = cv.CascadeClassifier("D:/software/python/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    # 获得范围
    face = face_detect.detectMultiScale(gray, 1.01, 5, 0, (100, 100), (300, 300))
    for x, y, w, h in face:
        cv.rectangle(img, (x, y, w, h), color=(0, 0, 255), thickness=1)
```
<div align="center" >
<p align="center">
    调用一个分类器（haarcascade_frontalface_alt2.xml），设置头像像素大小的范围，就能返回画框的四个要素（x, y, w, h）,也可使用这四要素画圆
</p>
<img src="https://pic.imgdb.cn/item/6507f703204c2e34d390e179.jpg">
</div>

### 06多个人脸位置检测
```shell
程序与05相同，侧视图头像更多
```
<div align="center" >
<img src="https://pic.imgdb.cn/item/6507f885204c2e34d391e2db.jpg">
</div>

### 07视屏人脸位置检测
<div align="center" >
<p align="center">
    打开视屏的同时，打开分类器进行人脸识别
</p>
<img src="https://pic.imgdb.cn/item/65080701204c2e34d3963ac3.webp">
</div>

### 08保存图片
<div>
<p>
    打开视屏，通过按键控制是否保存当前画面为图片，并给图片命名形式包含指定的名字
</p>
</div>

### 09数据训练
<div>
<p>
    使包含名字的图片能够形成图片与名字一一对应的效果
</p>
</div>

### 10人脸识别
<div>
<p>
    待续
</p>
</div>