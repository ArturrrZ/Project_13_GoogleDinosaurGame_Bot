import pyautogui
import time
#check current position of the mouse
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)

#Your own X,Y Coordinates
POSITION_OF_GOOGLEBROWSER_ICON_X=1254
POSITION_OF_GOOGLEBROWSER_ICON_Y=1059
#-------------------------------MAIN--------------------------MAIN---------------------------------MAIN--------------------------------#

pyautogui.click(POSITION_OF_GOOGLEBROWSER_ICON_X,POSITION_OF_GOOGLEBROWSER_ICON_Y)
time.sleep(2)
pyautogui.write('Hzxc')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('space')