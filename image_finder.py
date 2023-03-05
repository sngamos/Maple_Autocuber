from concurrent.futures import process
import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
from image_processing import image_process
import pytesseract
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#enter window name below
wincap = WindowCapture("Maplestory")

class potlines:
    image = None
    def __init__(self):
        self.screenshot()

    def screenshot(self):
        screenshot = wincap.get_screenshot()
        processed_img = image_process(screenshot)

        #cv.imshow('Potential lines', processed_img)
        self.image = processed_img
        #cv.waitKey(1)
    
    def get_ocr_result(self):
        self.screenshot()
        return pytesseract.image_to_string(self.image)

#pot=potlines()
#print(pot.get_ocr_result())
