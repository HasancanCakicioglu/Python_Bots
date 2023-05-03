import time

import keyboard
import pydirectinput
import mss
import pyautogui
import win32api
import win32con

image = "image/aim_main.png"
yellow_box = "image/yellow_box_2.png"

def click(x,y):
    pydirectinput.move(x,y)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def deneme(x,y):
    pydirectinput.move(x, y)


def locationOfYellowBoxes():
    locationYellowBoxes = pyautogui.locateOnScreen(yellow_box,confidence=0.2)
    return locationYellowBoxes

with mss.mss() as sct:
    monitor = {"top": 0, "left": 0, "width": sct.monitors[0]["width"], "height": sct.monitors[0]["height"]}

    # Ekran görüntüsünü al
    sct_img = sct.grab(monitor)

    a=30
    b=30
    while keyboard.is_pressed('q') == False:
        time.sleep(1)
        #boxes = locationOfYellowBoxes()
        deneme(a,b)
        a+=30
        b+=30
        #if boxes:
        #    print(boxes)
            #click(boxes[0]+30, boxes[1]+30)




