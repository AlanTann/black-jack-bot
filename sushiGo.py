from PIL import ImageGrab
import os
import time
import win32api, win32con

#Globals
# -------------------------

x_pad = 250
y_pad = 276
 
def screenGrab():
    #box = (250,276,1047,876)
    box = (x_pad+1, y_pad+1, x_pad+797, y_pad+600)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1])

#Get Coordinates
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

#Start the game
def startGame():
    #location of first menu
    mousePos((182, 225))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((193, 410))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((435, 470))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((167, 403))
    leftClick()
    time.sleep(.1)

def main():
    screenGrab()

if __name__ == '__main__':
    main()