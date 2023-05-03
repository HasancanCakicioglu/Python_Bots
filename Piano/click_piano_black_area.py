import time

import keyboard
import mss
import numpy as np
import pyautogui
import win32api
import win32con

image = "image/piano_main2.png"
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


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


with mss.mss() as sct:
    # Ekranın tamamını al
    monitor = {"top": Location[1], "left": Location[0], "width": Location[2], "height": Location[3]}

    x_out = Location[0]
    y_out = Location[1]
    h= Location[3]
    w = Location[2]

    x1, y1 = int(x_out+(w / 4) / 2), h + y_out - 250
    x2, y2 = int(x_out+(w/4)+(w/8)), h + y_out - 250
    x3, y3 = int(x_out+(w/2)+(w/8)), h + y_out - 250
    x4, y4 = int(x_out+w-(w/8)), h + y_out - 250

    while keyboard.is_pressed('q') == False:

        img = np.array(sct.grab(monitor))
        if img[y1-y_out, x1-x_out, 0] == 0:
            click(x1, y1)
        elif img[y2-y_out, x2-x_out, 0] == 0:
            click(x2, y2)
        elif img[y3-y_out, x3-x_out, 0] == 0:
            click(x3, y3)
        elif img[y4-y_out, x4-x_out, 0] == 0:
            click(x4, y4)


        elif img[y4-y_out-200, x4-x_out, 0] == 0:
            click(x4, y4-200)
        elif img[y3-y_out-200, x3-x_out, 0] == 0:
            click(x3, y3-200)
        elif img[y2-y_out-200, x2-x_out, 0] == 0:
            click(x2, y2-200)
        elif img[y1-y_out-200, x1-x_out, 0] == 0:
            click(x1, y1-200)









