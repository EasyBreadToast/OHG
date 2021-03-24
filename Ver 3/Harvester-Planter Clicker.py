import pydirectinput
import keyboard
import time

pydirectinput.PAUSE = 0.01

for i in range(5):
    time.sleep(1)
    print("Starting in", i)

while keyboard.is_pressed("l") == False:
    pydirectinput.click()
    
