# Add your Python code here. E.g.
from microbit import *

image_zer = Image('09990:09090:09090:09090:09990')
image_one = Image('00900:09900:00900:00900:09990')
image_two = Image('09990:00090:09990:09000:09990')
image_thr = Image('09990:00090:09990:00090:09990')
image_for = Image('09090:09090:09990:00090:00090')
image_fiv = Image('09990:09000:09990:00090:09990')
image_six = Image('09990:09000:09990:09090:09990')
image_svn = Image('09990:09090:00090:00090:00090')
image_eit = Image('09990:09090:09990:09090:09990')
image_nin = Image('09990:09090:09990:00090:09990')
numbers = [image_zer,image_one,image_two,image_thr,image_for,image_fiv,image_six,image_svn,image_eit,image_nin]
index = 0
pushing_a = False
pushing_b = False
while True:
    if button_a.is_pressed():
        if pushing_a is False:
            index += 1
            if index > 9:
                index = 0
        pushing_a = True
    else:
        pushing_a = False

    if button_b.is_pressed():
        if pushing_b is False:
            index -= 1
            if index > 0:
                index = 9
        pushing_b = True
    else:
        pushing_b = False

    display.show(numbers[index], delay=0, wait=True, loop=False, clear=False)