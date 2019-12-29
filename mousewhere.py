import pyautogui
import sys
import time

def mousewhere():
        while(1):
            print("\r", end = '')
            print(pyautogui.position(), end = '')
