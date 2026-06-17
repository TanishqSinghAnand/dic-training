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
    root = os.getcwd()
    imgPath = os.path.join(root, r'Images\chotu.jpeg')
    img = cv.imread(imgPath)
    #convert bgr to rgb
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    #let's extract the eye region
    eyeRegion = imgRGB[186:206, 179:234] #y , x

    dy = 206-186
    dx = 234-179
    startY = 140
    startX = 213
    imgRGB[startY:startY+dy, startX:startX+dx] = eyeRegion
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

# readAndWriteSinglePixel()
readAndWritePixelRegion()
