# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread("text1.jpg")

# 灰度转换
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 显示灰度
cv.imshow("gray", gray_img)
# 保存图片
cv.imwrite("gray_text1.jpg", gray_img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()
