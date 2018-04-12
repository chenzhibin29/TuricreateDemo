#coding=utf-8
import cv2 
import time
import threading

if __name__ == '__main__':

    cv2.namedWindow("camera",1)
    #开启ip摄像头
    video="http://admin:admin@192.168.1.13:8081/"
    capture =cv2.VideoCapture(video)
    
    img_num = 1
    img_step=10
    while True:
        success,img = capture.read()
        cv2.imshow("camera",img)

        if(img_num % 10==0):
            filename = "/home/chen/Desktop/demo-python-image-classification-master/image/dianji/dianji%s.jpeg" % img_num
            cv2.imwrite(filename,img)
        img_num=img_num+1
        if img_num>2000:
            break
        
    #按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
        key = cv2.waitKey(10) 

        if key == 27:
        #esc键退出
            print("esc break...")
            break
     
    capture.release()
    cv2.destroyWindow("camera")
