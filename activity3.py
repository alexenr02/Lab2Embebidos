from grove_rgb_lcd import *
import time
import grovepi
from grovepi import *
import math
# Connect the Grove Temperature Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 0

button = 4      #Port for Button
pinMode(button,"INPUT")     # Assign mode for Button as input


while True:
    print("temp =", temp)
    time.sleep(.5)
    temp = grovepi.temp(sensor,'1.1')  
    text=str(temp)
    try:
        
        button_status= digitalRead(button)  #Read the Button status
        if button_status:   #If the Button is in HIGH position, run the program
           setRGB(0,255,0)
           print("running")
           
           setText(text)
           
            # print "\tBuzzing"         
        else:       #If Button is in Off position, print "Off" on the screen
           setRGB(255,0,0)
           setText("Presiona el \nboton")
           print "Off" 
           
           
    except KeyboardInterrupt:   # Stop the buzzer before stopping
        break
    except (IOError,TypeError) as e:
        print("Error")        