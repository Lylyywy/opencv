# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread("text21.jpg")
print("未修改", img.shape)
cv.imshow("read", img)
h, w = img.shape[:2]

resize_img = cv.resize(img, dsize=(200, 200))       #修改尺寸大小为（200,200）
resize_img1 = cv.resize(img, dsize=(w//4, h//4))    #缩小为原来的1/4
# 显示
cv.imshow("resize", resize_img1)
# 打印尺寸大小
print("修改后", resize_img1.shape)

# 等待
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()
