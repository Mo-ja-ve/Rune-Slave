import pyautogui
import keyboard
import importlib
import autoclicker
import sys
import mousewhere

auto = pyautogui

#mousewhere.mousewhere()

#def health_check():
    #img = snashot.save('screengrab.png')

pyautogui.PAUSE = 1

##printf(auto.size())

#for i in range(1):
#   health_check()

while(1):
    if keyboard.is_pressed("1"):
        autoclicker.autoclicker()
    if keyboard.is_pressed("3"):
        sys.exit(0)

