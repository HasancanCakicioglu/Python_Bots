import time

import keyboard
import numpy as np
import mss
import pyautogui
import win32api
import win32con

image = "image/main.png"
money = "image/money.png"
go = "image/readygo.png"
guillotine = "image/guillotine.png"

Location = None
while keyboard.is_pressed('q') == False:
    Location = pyautogui.locateOnScreen(image, confidence=0.5)
    print("searching...")
    if Location is not None:
        print(Location)
        break

if Location is None:
    print("Image not found, exiting...")
    exit()

def locationOfMoney(region):
    locationMoney = pyautogui.locateOnScreen(money, confidence=0.5,region=region)
    print(locationMoney)
    return locationMoney

def locationOfGiyotin(region):
    locationGiyotin = pyautogui.locateOnScreen(guillotine, confidence=0.97,region=region)
    return locationGiyotin

def locationOfreadyGo(region):
    locationReadyGo = pyautogui.locateOnScreen(go, confidence=0.5,region=region)
    return locationReadyGo


def clickAndPul(x,y,h,rightX,rightY):
    win32api.SetCursorPos((x,y+h))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.12)
    win32api.SetCursorPos((int(rightX),int(rightY)))
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click(x,y):
    win32api.SetCursorPos((int(x),int(y)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

with mss.mss() as sct:
    # Ekranın tamamını al
    monitor = {"top": Location[1], "left": Location[0], "width": Location[2], "height": Location[3]}

    x1 = Location[0]
    y1 = Location[1]
    width = Location[2]
    height = Location[3]

    regionMoney = (x1,y1, width, height)
    #regionGo = (int(x1-(width/2)),int(y1-(height/2)), width, height)
    #regionGiyotin = (int(x1+(width/2.5)),int(y1),int(width/4),height)
    regionGiyotin = (int(x1+(width/4)), y1,int(width-(width/4)), height)

    rightPlaceWaitX  = x1 + width - (width/3)
    rightPlaceWaitY = y1 + (height/2)

    while keyboard.is_pressed('q') == False:

        # Ekran görüntüsü al
        img = np.array(sct.grab(monitor))

        pyautogui.moveTo(rightPlaceWaitX,rightPlaceWaitY)


        locMoney = locationOfMoney(regionMoney)
        giyotin = locationOfGiyotin(regionGiyotin)

        if giyotin:
            if locMoney:
                clickAndPul(locMoney[0],locMoney[1],int(locMoney[3]/2),rightPlaceWaitX,rightPlaceWaitY)

        locReady = locationOfreadyGo(regionMoney)
        if locReady:
            click(locReady[0]+(locReady[2]/2),locReady[1]+(locReady[3]/2))







