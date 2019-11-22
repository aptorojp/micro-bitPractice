# Add your Python code here. E.g.
from microbit import *

cordinate = [0,0]
display.set_pixel(0,0,9)
pushing_a = False
pushing_b = False
while True:
    if button_a.is_pressed():
        if pushing_a is False:
            display.set_pixel(cordinate[0],cordinate[1],0) #delete pre val
            cordinate[1] += 1
            if cordinate[1] > 4:
                cordinate[1] = 0
            display.set_pixel(cordinate[0],cordinate[1],9) #set new val
        pushing_a = True
#        sleep(100)
    else:
        pushing_a = False
    if button_b.is_pressed():
        if pushing_b is False:
            display.set_pixel(cordinate[0],cordinate[1],0) #delete pre val
            cordinate[0] += 1
            if cordinate[0] > 4:
                cordinate[0] = 0
            display.set_pixel(cordinate[0],cordinate[1],9) #set new val
        pushing_b = True
#        sleep(100)
    else:
        pushing_b = False