# Add your Python code here. E.g.
from microbit import *
import math

while True:
    
    x=accelerometer.get_x()
    y=accelerometer.get_y()
    z=accelerometer.get_z()
    #print("x: ",x)
    #print("y: ",y)
    #print("z: ",z)
    presses=button_a.get_presses()
    if math.sqrt((x*x)+(y*y)) > 1000:
        pressed=False
        for i in range(9,0,-1):
            display.show(i)
            sleep(1000)
            if button_a.get_presses()>presses:
                pressed=True
                display.show(" ")
                break

        
        if not(pressed):
            print("help")
            display.show(" ")
    sleep(250)