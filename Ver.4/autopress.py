import pydirectinput
import time
import keyboard
from threading import Thread, Lock

pydirectinput.PAUSE = 0.0001

class Clickers():
    
    #Thread Properties

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    # main logic controller
    def run(self):
        while not self.stopped:
            pydirectinput.press("f")
            pydirectinput.click()
            pass

