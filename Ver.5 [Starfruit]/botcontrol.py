import pydirectinput
import time
import keyboard
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
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    # main logic controller
    def run(self):

        #Move the mouse
        time.sleep(1)
        pydirectinput.move(1,2)
        pydirectinput.click(self.x,self.y)

        while not self.stopped:
            
            #Move mouse to onion
            pydirectinput.move(1,2)
            pydirectinput.click(self.x,self.y)
            
            #Wait for the mouse
            time.sleep(0.2)

            #Drag mouse
            for move in range(300):
                pydirectinput.move(3,0)
                time.sleep(0.007)

            #Move next
            pydirectinput.keyDown("s")
            time.sleep(0.2)
            pydirectinput.keyUp("s")
            time.sleep(0.5)
            print("Complete")
            
            pass

