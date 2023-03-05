import pyautogui
import time
import keyboard



        

def time_to_start():
    for i in range(5):
        print(5-i)
        time.sleep(1)

def click():
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('enter')


