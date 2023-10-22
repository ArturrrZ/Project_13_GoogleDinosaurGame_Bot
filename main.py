import pyautogui
#install open-cv to use confidence function
#pip install opencv-python

import time
#check current position of the mouse
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)


#-------------------------------MAIN--------------------------MAIN---------------------------------MAIN--------------------------------#
def old_version_to_find_google_icon():

    #Your own X,Y Coordinates
    POSITION_OF_GOOGLEBROWSER_ICON_X=1254
    POSITION_OF_GOOGLEBROWSER_ICON_Y=1059
    #OLD VERSION WITH COORDINATES
    pyautogui.click(POSITION_OF_GOOGLEBROWSER_ICON_X,POSITION_OF_GOOGLEBROWSER_ICON_Y)
    time.sleep(2)
    pyautogui.write('Hzxc')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('space')

google=pyautogui.locateCenterOnScreen('google_icon.png',confidence=0.8)
print(google.x)
print(google.y)

time.sleep(1)

pyautogui.click(google.x,google.y)