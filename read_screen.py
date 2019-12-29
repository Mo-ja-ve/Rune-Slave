import pyautogui
auto = pyautogui
import sys


snapshot = pyautogui.screenshot()

#snapshot.save('/home/user/Documents/rune_slave/screenshot/screengrab.png')    

print(auto.locateOnScreen('Screenshot_2019-12-01_17-30-07.png', confidence=0.9))
