# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread("text21.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)     #RGB转换为GARY
bgr_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)       #RGB转换为BGR
hsv_img = cv.cvtColor(img, cv.COLOR_RGB2HSV)       #RGB转换为HSV
ycrcb_img = cv.cvtColor(img, cv.COLOR_RGB2YCrCb)   #RGB转换为YCrCb

# 显示
cv.imshow("gray", gray_img)
cv.imshow("bgr", bgr_img)
cv.imshow("hsv", hsv_img)
cv.imshow("ycrcb", ycrcb_img)
# 保存图片
#cv.imwrite("gray_text1.jpg", gray_img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()
