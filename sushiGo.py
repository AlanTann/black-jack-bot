from PIL import ImageGrab
import os
import time

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
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()