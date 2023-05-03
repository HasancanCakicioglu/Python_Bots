import pyautogui

key  = "../../assets/images/cal8key.png"

button7location = pyautogui.locateOnScreen(key)
print(button7location)

button7point = pyautogui.center(button7location)
button7x, button7y = button7point
pyautogui.click(button7x, button7y)


pyautogui.click(key)


x, y = pyautogui.locateCenterOnScreen(key)
pyautogui.click(x, y)

# resimden kaç tane varsa ekranda hepsinin konumunu döndürür
for pos in pyautogui.locateAllOnScreen(key):
      print("pos = "+str(pos))

# belirli bir bölümde arama yapar(performans )
pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400), confidence=0.9)