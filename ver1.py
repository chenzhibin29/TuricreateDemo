#coding=utf-8
import cv2 
import time
import threading
import os
import turicreate as tc
from Tkinter import *
if __name__ == '__main__':

   
   #button call reg()
    def reg():
        ip_add=ip.get()
        cv2.namedWindow("camera",1)
        video="http://admin:admin@%s:8081/" % ip_add
        #print'%s' %video
    
        #open video
        capture =cv2.VideoCapture(video)
     
        img_num = 1
        img_step=100
        #load trained model
        loaded_model=tc.load_model('mymodel2')
    
        while True:
            success,img = capture.read()
            cv2.imshow("camera",img)
            #filename1 is going to used pictures folder
            filename1 = "/home/chen/Desktop/demo-python-image-classification-master/image/computer"
            if(img_num%img_step==0):
                
               #filename is  to be saved pictures,100 frame save 1 picture
                filename = "/home/chen/Desktop/demo-python-image-classification-master/image/computer/frames_%s.jpeg" % img_num
                cv2.imwrite(filename,img)
                #print(os.path.exists(filename1))
                #filename1  is or not exists
                if os.path.exists(filename1):          
                    prediction1=loaded_model.predict(tc.image_analysis.load_images(filename1, with_path=True))
                    print(prediction1)
                    result.config(text=prediction1)
                    result.update()
                os.remove(filename)
            img_num=img_num+1
            #save 10 pictures,and auto end
            if img_num>1000:
                break
            key = cv2.waitKey(10)
            if key == 27:
                #esc键退出
                    print("esc break...")
                    break

        capture.release()
        cv2.destroyWindow("camera")  
   #GUI design       
    root=Tk()
    input_ip=Label(root,text="input ip:")
    input_ip.grid(row=0,column=0,sticky='w')
    #input ip
    ip=Entry(root)
    ip.insert(10,'192.168.1.105')
    ip.grid(row=0,column=1,sticky='E')
    #click button'ok' call reg()
    ok=Button(root,text="ok",command=reg)
    ok.grid(row=1,column=0,sticky='E')
    #output prediction
    pred=Label(root,text='predictions:')
    pred.grid(row=2,column=0,sticky='W')
    result=Label(root,text='')
    result.grid(row=2,column=1,sticky='E')
    root.mainloop()
    

    
   
