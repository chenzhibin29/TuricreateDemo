import turicreate as tc
import os
import random
import numpy as np
import shutil

if __name__=='__main__':
    a=np.arange(0,1000,5)
    print(a)
    for b in a:
        filename = "/home/chen/Desktop/demo-python-image-classification-master/image/compter/compter_%s.jpeg" % b
    filename1="/home/chen/Desktop/demo-python-image-classification-master/image/computer"
    shutil.move(filename,filename1)
