# 导入cv模块
import cv2 as cv

# 读取图片：imread(filename,flags)
img = cv.imread("text2.jpg")        #默认返回彩色图像（R, G, B）
img1 = cv.imread("text2.jpg", 0)    #返回灰度值
img2 = cv.imread("text2.jpg", 4)    #返回所有颜色
img3 = cv.imread("text2.jpg", 128)  #忽略任何旋转
img4 = cv.imread("text2.jpg", -1)   #返回包含透明度（Alpha）通道的加载图像（R, G, B, Alpha）Alpha为0时完全透明
# 显示图片
cv.imshow("img", img)
cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("img4", img4)
# 等待，0表示一直等待，数字表示等待毫秒
cv.waitKey(0)
# 释放所有窗口内存
cv.destroyAllWindows()
