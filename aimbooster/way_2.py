import time

import keyboard
import numpy as np
import mss
import pyautogui

image = "image/aimbooster_main.png"
Location = None
while keyboard.is_pressed('q') == False:
    Location = pyautogui.locateOnScreen(image, confidence=0.2)
    print("searching...")
    if Location is not None:
        print(Location)
        break

if Location is None:
    print("Image not found, exiting...")
    exit()

with mss.mss() as sct:
    # Ekranın tamamını al
    monitor = {"top": Location[1], "left": Location[0], "width": Location[2], "height": Location[3]}

    x1 = Location[0]
    y1 = Location[1]

    x_c =0
    y_c =0

    while keyboard.is_pressed('q') == False:
        
        # Ekran görüntüsü al
        img = np.array(sct.grab(monitor))

        # Mavi rengini temsil eden 195 sayısı ile karşılaştır
        blue_pixels = np.where(img[:,:,0] == 195)

        # Eşleşen piksellerin koordinatlarını yazdır

        for y, x in zip(blue_pixels[0], blue_pixels[1]):
            if abs(x_c - (x+x1))<20 and abs(y_c-(y+y1))<20:
                continue
            pyautogui.click(x + x1, y + y1)

            x_c = x+x1
            y_c = y+y1







