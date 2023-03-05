import imghdr
import cv2 as cv
import numpy as np
import os
from time import time
import win32gui, win32ui, win32con
import pyautogui

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))



class WindowCapture:

    w = 0
    h = 0 
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    def __init__(self,window_name):

        self.hwnd = win32gui.FindWindow(None, window_name)

        if not self.hwnd: 
            raise Exception("Window not found: {}".format(window_name))

        self.w =167
        self.h = 58

        self.cropped_x = 17
        self.cropped_y = 213

        
    def get_screenshot(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (self.cropped_x,self.cropped_y), win32con.SRCCOPY)\

        #save the screenshot    
        #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h,self.w,4 )


        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        img = np.ascontiguousarray(img)

        return img
