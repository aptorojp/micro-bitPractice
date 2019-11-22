# Add your Python code here. E.g.
from microbit import *

i = [0,0]
while True:
    for row in range(5):
        for col in range(5):
            i[0] = row
            i[1] = col
            display.set_pixel(i[0],i[1],max(i))