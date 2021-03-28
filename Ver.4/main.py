import cv2 as cv
import time
import keyboard
from windowcapture import WindowCapture
from mousecontrol import Mouse
from botcontrol import Bot
from autopress import Clickers

print("Press Q to stop")

windowname = "Roblox"

# initialize the WindowCapture class
wincap = WindowCapture(windowname)
mouse = Mouse((wincap.offset_x, wincap.offset_y), (wincap.w, wincap.h))
bot = Bot()
clickers = Clickers()


#Start Window Capture thrread.s
wincap.start()
bot.start()
clickers.start()


#Communicator
while(True):

    # if we don't have a screenshot yet, don't run the code below this point yet
    if wincap.screenshot is None:
        continue

    #esfSend captured screenshot  to mousecontrol.py
    mouse.function(wincap.screenshot)
    
    #Send mouse coords to botcontrol.py
    bot.getMouseCoords(mouse.mouseXaxies,mouse.mouseYaxies)


    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if keyboard.is_pressed('q'):
        print("Shutting down")
        clickers.stop()
        bot.stop()
        wincap.stop()
        cv.destroyAllWindows()
        break

