# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread("text21.jpg")
cv.imshow("read", img)

# 坐标(x:起点到图像最左边的距离，y:起点到图像上边距离，w:起点向右走的距离，h:起点向下走的距离，r:圆的半径)
x, y, w, h = 100, 200, 10, 100
# 绘制
cv.rectangle(img, (x, y, w, h), color=(0, 0, 255), thickness=1)
cv.circle(img, center=(x, y), radius=100, color=(0, 255, 0), thickness=2)
# 显示
cv.imshow("draw", img)
# 等待(按q退出)
while True:
    if ord("q") == cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()
