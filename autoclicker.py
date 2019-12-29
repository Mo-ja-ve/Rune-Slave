import pyautogui                 #                                                           
import tkinter                   #debug error suggested I had to add this, allows mouse clicks to work on linux                                                                      
import keyboard                  #adds ability to check for keystroke                                                          
import sys                       #adds ability to use sys.exit()

def autoclicker():

    auto = pyautogui

    auto.PAUSE = 1.5

    stop = 0

    while stop != 1:
        if keyboard.is_pressed('2'):
            break
        auto.PAUSE = 1.5
        if keyboard.is_pressed('2'):
            break  
        auto.click(button='left')
        if keyboard.is_pressed('2'):
            break
