import time
import timeit

import pyautogui
import keyboard

Location=None

image = "image/aimbooster_main.png"



while keyboard.is_pressed('q') == False:
    Location = pyautogui.locateOnScreen(image, confidence=0.2)
    print("searching...")
    if Location is not None:
        print(Location)
        break

if Location is None:
    print("Image not found, exiting...")
    exit()

while keyboard.is_pressed('q') == False:


    #x1,y1,width,height
    pic = pyautogui.screenshot(region=Location)
    width,height = pic.size
    x1, y1 = Location[0],Location[1]

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 195:
                pyautogui.click(x+x1,y+y1)

                break





