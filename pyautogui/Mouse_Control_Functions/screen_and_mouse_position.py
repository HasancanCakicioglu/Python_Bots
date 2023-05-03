import time

import pyautogui,sys


print(pyautogui.size())
print(pyautogui.position())
print(pyautogui.onScreen(1920, 1080))
print(pyautogui.onScreen(1919, 1079))


print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='',flush=True)
except KeyboardInterrupt:
    print('\n')

if __name__ == '__main__':
    pass