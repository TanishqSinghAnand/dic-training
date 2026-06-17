import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt


def readAndWriteSinglePixel():
    root = os.getcwd()
    imgPath = os.path.join(root, r'Images\Cat_Hint.png')
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

# def readAndWritePixelRegion():
#     root = os.getcwd()
#     imgPath = os.path.join(root, r'Images\Cat_Small.png')
#     img = cv.imread(imgPath)
#     #convert bgr to rgb
#     imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#     plt.figure()
#     plt.imshow(imgRGB)
#     plt.show()
#     #let's extract the eye region
#     eyeRegion = imgRGB[160:203, 130:190] #y , x

#     dy = 203-160
#     dx = 190-130
#     startY = 120
#     startX = 170
#     imgRGB[startY:startY+dy, startX:startX+dx] = eyeRegion
#     plt.figure()
#     plt.imshow(imgRGB)
#     plt.show()


readAndWriteSinglePixel()





# readAndWritePixelRegion()