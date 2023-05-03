import pyautogui
key  = "../../assets/images/cal8key.png"


# grayscale = True // %30 civarı performans kazandırır ancak doğruluğu düşürür
button7location = pyautogui.locateOnScreen(key, grayscale=True)
print(button7location)

#PİXEL MATCHING

# bu 100,200 noktasındaki rgb renk değerlerini döndürür
im = pyautogui.screenshot()
print(im.getpixel((100, 200)))

# bu 100,200 noktasındaki rgb renk değerlerini döndürür
pix = pyautogui.pixel(100, 200)
print(pix)

# bu o piksel bu rgb renge eşitmi
match = pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))
print(match)


# üstekinin tolerans verilmiş hali
match = pyautogui.pixelMatchesColor(100, 200, (130, 135, 144),tolerance=10)
print(match)