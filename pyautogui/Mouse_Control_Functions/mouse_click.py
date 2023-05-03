import pyautogui


pyautogui.click(x=100, y=200)
pyautogui.click(button='right')
pyautogui.click(clicks=2)  # double-click the left mouse button
pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks
pyautogui.doubleClick()


