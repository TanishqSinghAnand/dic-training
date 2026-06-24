import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def PureColours():
    zeros = np.zeros((100,100))
    ones = np.ones((100,100))
    bImg = cv.merge((zeros, zeros, 255*ones))
    gImg = cv.merge((zeros, 255*ones, zeros))
    rImg = cv.merge((255*ones, zeros, zeros))
    wImg = cv.merge((255*ones, 255*ones, 255*ones))
    kImg = cv.merge((zeros, zeros, zeros))

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('blue')
    plt.subplot(232)
    plt.imshow(gImg)
    plt.title('green')
    plt.subplot(233)
    plt.imshow(rImg)
    plt.title('red')
    plt.subplot(234)
    plt.imshow(wImg)
    plt.title('white')
    plt.subplot(235)
    plt.imshow(kImg)
    plt.title('black')
    plt.show()
    #task plot green, blue, red, white and black pictures!

PureColours()