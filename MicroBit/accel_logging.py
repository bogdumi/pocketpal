# Add your Python code here. E.g.
from microbit import *


while True:
    display.scroll('Hello, World!')
    display.show(Image.HEART)
    
    log=open("accellog.txt",'w')
    while True:
        readingx = accelerometer.get_x()
        readingy = accelerometer.get_y()
        readingz = accelerometer.get_z()
        my_file.write("\n"+str((readingx,readingy,readingz)))
        sleep(100)

    #sleep(2000)

