# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread("text1.jpg")
cv.imshow("read", img)
# 修改尺寸
resize_img = cv.resize(img, dsize=(200, 200))
# 显示原图
cv.imshow("resize", resize_img)
# 打印尺寸大小
print("未修改", img.shape)
print("修改后", resize_img.shape)

# 等待(按q退出)
while True:
    if ord("q") == cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()
