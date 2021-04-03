import pyautogui
import pydirectinput
import time
import keyboard

pyautogui.PAUSE = 0.001

while keyboard.is_pressed("q") == False:
    pydirectinput.press('/')
    time.sleep(1)
    pyautogui.write("HONK")
    time.sleep(1)
    pydirectinput.press("enter")
    time.sleep(1)