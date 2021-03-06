import pydirectinput
import time 
from threading import Thread, Lock



class Bot():
    
    x = 0
    y = 0
    toggle = True

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
            
            for self.clicks in range(64):
                pydirectinput.move(1,1)
                pydirectinput.click(self.x,self.y)
                pydirectinput.press("f")
                time.sleep(0.3)

            pydirectinput.keyDown("s")
            time.sleep(1)
            pydirectinput.keyUp("s")
            print("Complete")

            pass

