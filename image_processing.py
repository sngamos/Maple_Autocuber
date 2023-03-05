import cv2 as cv
from numpy import interp


def invert_image(image):
    return cv.bitwise_not(image)

def greyscale(image):
    return cv.cvtColor(image,cv.COLOR_BGR2GRAY)

def adjust_threshhold(gray_image):
    thresh, img_bw = cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
    return img_bw

def adjust_scale(image):
    return cv.resize(image,None,fx=3,fy=3,interpolation=cv.INTER_CUBIC)


def image_process(image):
    image = invert_image(image)
    image = greyscale(image)
    image = adjust_threshhold(image)
    image = adjust_scale(image)
    return image