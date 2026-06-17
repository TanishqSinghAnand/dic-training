import cv2 as cv
import os
import numpy as np

def readImage():
    imagePath = "D:\Coding\DIC\opencv\Images\Cat_Small.png"
    img = cv.imread(imagePath)
    debug = 1
    cv.imshow("Cute Cat", img)
    cv.waitKey(0)

readImage()

def writeImage():
    imagePath = "D:\Coding\DIC\opencv\Images\Cat_Small.png"
    img = cv.imread(imagePath)
    debug = 1
    savePath = "D:\Coding\DIC\opencv\Images\Cat_Small_copy.png"
    cv.imwrite(savePath, img)

writeImage()