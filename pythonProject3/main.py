import pyautogui
import time
time.sleep(10)
for i in range(50):
    pyautogui.typewrite("Hello ")
    pyautogui.press("enter")