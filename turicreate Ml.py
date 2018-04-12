import turicreate as tc
img_folder = '/home/chen/Desktop/demo-python-image-classification-master/image'
data = tc.image_analysis.load_images(img_folder, with_path=True)
data['label'] = data['path'].apply(lambda path: 'doraemon' if 'doraemon' in path else 'walle')
data.save('doraemon-walle.sframe')
train_data, test_data = data.random_split(0.8, seed=2)
model = tc.image_classifier.create(train_data, target='label')
predictions=model.predict(test_data)
predictions
metrics=model.evaluate(test_data)
print(metrics['accuracy'])
test_data['label']
test_data[test_data['label']!=predictions]
wrong_pred_img_path=test_data[predictions!=test_data['label']][0]['path']
img=tc.Image(wrong_pred_img_path)
img.show()
image2='/home/chen/Desktop/demo-python-image-classification-master/image/test/timg.jpeg'
data3 = tc.image_analysis.load_images(image2, with_path=True)
prediction1=model.predict(data3)
prediction1
loaded_data=tc.load_sframe('doraemon-walle.sframe')
model.save('mymodel')
loaded_model=tc.load_model('mymodel')

#coding=utf-8
import cv2 
import time
import threading
def fun():
    num=0;
    num = num+1
    filename = "/home/chen/Desktop/demo-python-image-classification-master/image/test/frames_%s.jpg" % num
    cv2.imwrite(filename,img)
    
if __name__ == '__main__':

    cv2.namedWindow("camera",1)
    #开启ip摄像头
    video="http://admin:admin@192.168.1.13:8081/"
    capture =cv2.VideoCapture(video)

    #num = 0;
    while True:
        success,img = capture.read()
        cv2.imshow("camera",img)

    #按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
        key = cv2.waitKey(10) 

        if key == 27:
        #esc键退出
            print("esc break...")
            break
        else:
            key=threading.Timer(5.0,fun)
            key.start()


    capture.release()
    cv2.destroyWindow("camera")



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
    img_step=100
    while True:
        success,img = capture.read()
        cv2.imshow("camera",img)

        if(img_num%img_step==0):
            filename = "/home/chen/Desktop/demo-python-image-classification-master/image/test/frames_%s.tiff" % img_num
            cv2.imwrite(filename,img)
        img_num=img_num+1
        if img_num>1000:
            break
        
    #按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
        key = cv2.waitKey(10) 

        if key == 27:
        #esc键退出
            print("esc break...")
            break
     
    capture.release()
    cv2.destroyWindow("camera")



#coding=utf-8
import cv2 
import time
import threading
import os
import turicreate as tc
from Tkinter import *
if __name__ == '__main__':

    cv2.namedWindow("camera",1)
    #开启ip摄像头
    
    def reg():
        s=e.get()
        
    video="%s/" % s
    capture =cv2.VideoCapture(video)
    
    img_num = 1
    img_step=100
    loaded_model=tc.load_model('mymodel2')
    
    while True:
        success,img = capture.read()
        cv2.imshow("camera",img)
        filename1 = "/home/chen/Desktop/demo-python-image-classification-master/image/computer"
        if(img_num%img_step==0):
            print('writing files...')
            filename = "/home/chen/Desktop/demo-python-image-classification-master/image/computer/frames_%s.jpeg" % img_num
            cv2.imwrite(filename,img)
            print(os.path.exists(filename1))
            if os.path.exists(filename1):          
                print('predicting...')
                prediction1=loaded_model.predict(tc.image_analysis.load_images(filename1, with_path=True))
                print(prediction1)
            os.remove(filename)
        img_num=img_num+1
        if img_num>1000:
            break
        key = cv2.waitKey(10)
      
       
    #按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
       

        if key == 27:
        #esc键退出
            print("esc break...")
            break
     
    capture.release()
    cv2.destroyWindow("camera")
