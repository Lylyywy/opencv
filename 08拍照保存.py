#导入cv模块
import cv2 as cv

#读取摄像头
cap = cv.VideoCapture(0)
num = 1
#循环
while(cap.isOpened):
    ret_flag, Vshow = cap.read()
    cv.imshow("capture_Text", Vshow)
    k = cv.waitKey(1) & 0xFF
    if k == ord(" "):
        cv.imwrite("D:/ly/First/python/opencv/image/"+str(num)+".ly"+".jpg", Vshow)
        print("success to save"+str(num)+".jpg")
        print("-----------------")
        num += 1
    elif k == ord("s"):
        break

#释放摄像头
cap.release()
#释放内存
cv.destroyAllWindows()
