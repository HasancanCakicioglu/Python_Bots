import pyautogui


pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.moveTo(200, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
pyautogui.moveTo(300, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
pyautogui.moveTo(400, 100, 2, pyautogui.easeInBounce)   # bounce at the end
pyautogui.moveTo(500, 100, 2, pyautogui.easeInElastic)  # rubber band at the end