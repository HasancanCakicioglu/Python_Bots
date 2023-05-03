import pyautogui

pyautogui.write('Hello world!')                 # prints out "Hello world!" instantly
pyautogui.write('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character