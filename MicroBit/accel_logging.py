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
    if math.sqrt((x*x)+(y*y)+((z*z))) > 1000:
        print("help")
    sleep(250)