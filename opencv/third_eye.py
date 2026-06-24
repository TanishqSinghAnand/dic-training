import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt


def readAndWriteSinglePixel():
    root = os.getcwd()
    imgPath = os.path.join(root, r'Images\chotu.jpeg')
    img = cv.imread(imgPath)
    #convert bgr to rgb
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    eyePixel = imgRGB[183, 166] # note it's y,x
    debug = 1
    imgRGB[183, 166] = (255,0,0)
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

def readAndWritePixelRegion():
    imgPath = "./Images/chotu.jpeg"
    img = cv.imread(imgPath)

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    eye = imgRGB[186:206, 179:234] 

    x_start = 213
    y_start = 140
    
    dy = 206-186
    dx = 234-179
    
    imgRGB[y_start:y_start+dy, x_start:x_start+dx] = eye
    
    plt.figure()
    plt.title("3 eyed chotu")
    plt.imshow(imgRGB)
    plt.show()


# readAndWriteSinglePixel()
readAndWritePixelRegion()