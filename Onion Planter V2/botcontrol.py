import pyautogui
import pydirectinput
import time 
from threading import Thread, Lock

pydirectinput.PAUSE = 0.0001

class Bot():
    
    x = 0
    y = 0
    toggle = True
    contour = False

    #Bot Actions/Values
    
    def getMouseCoords(self,xInput,yInput):
        if self.toggle == True:
            self.x = xInput
            self.y = yInput
        else:
            pass

    #Thread Properties

    def start(self):
        t = Thread(target=self.run)
        t.start()

    # main logic controller
    def run(self):
        while True:
            
            #Move mouse to onion
            pydirectinput.move(1,1)
            pydirectinput.click(self.x,self.y)
            
            #Wiat for the mouse
            time.sleep(0.2)

            #Harvesting
            pydirectinput.keyDown("f")
            for move in range(321):
                pydirectinput.move(2,0)
                time.sleep(0.005)
            pydirectinput.keyUp("f")

            #Planting
            pydirectinput.mouseDown()
            for move in range(321):
                pydirectinput.move(-2,0)
                time.sleep(0.005)
            pydirectinput.mouseUp()

            #Move next
            pydirectinput.keyDown("s")
            time.sleep(0.2)
            pydirectinput.keyUp("s")
            time.sleep(0.5)
            print("Complete")
            
            pass

