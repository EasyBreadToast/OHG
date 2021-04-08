import pyautogui
import keyboard
import autoit


# x and y are coordinates on the screen, the third param should be speed(?) I have played with it 
# and found no difference in the execution of the code.

while True:
    if keyboard.is_pressed("t"):
        autoit.mouse_move(100, 1000, 100)