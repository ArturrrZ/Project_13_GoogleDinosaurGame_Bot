import pyautogui
import time
#check current position of the mouse
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)

pyautogui.click(1254,1059)
time.sleep(2)
pyautogui.write('Hzxc')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('space')