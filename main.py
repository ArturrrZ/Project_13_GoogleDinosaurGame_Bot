import pyautogui
import keyboard
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


#detect cactus

def old_version_with_image_recognition():
    google = pyautogui.locateCenterOnScreen('google_icon.png', confidence=0.8)

    time.sleep(1)

    pyautogui.click(google.x, google.y)

    time.sleep(1)

    pyautogui.write('https://elgoog.im/dinosaur-game/')
    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.press('space')

    end=False
    while not end:

        cactus_big = pyautogui.locateCenterOnScreen('cactus_big.png',confidence=0.5)
        if cactus_big is not None:
            # print('I found the CACTUS')
            # print(f'His coordinates: {cactus_big.x,cactus_big.y}')
            if cactus_big.x < 500:
                pyautogui.press('space')
        else:
            # print('There is no big cactus')
            pass

        cactus_small_part = pyautogui.locateCenterOnScreen('small.png', confidence=0.5)
        if cactus_small_part is not None:
            print('I found the CACTUS')
            print(f'His coordinates: {cactus_small_part.x, cactus_small_part.y}')
            if cactus_small_part.x < 500:
                pyautogui.press('space')
        else:
            # print('There is no big cactus')
            pass

def new_script_with_pixel_recognition():
    time.sleep(3)


    end=False
    while not end:
        #stop the game
        if keyboard.is_pressed('q'):
            end=True
        y_positions=[678,750]
        for each in y_positions:

            r, g, b = pyautogui.pixel(350, each)
            if r < 200:
                pyautogui.press('space')

def find_google_icon_by_image():
    #and start the game
    google = pyautogui.locateCenterOnScreen('google_icon.png', confidence=0.8)

    time.sleep(1)

    pyautogui.click(google.x, google.y)

    time.sleep(1)
    pyautogui.hotkey('ctrl','T')

    time.sleep(1)

    pyautogui.write('https://elgoog.im/dinosaur-game/')
    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.press('space')



find_google_icon_by_image()
new_script_with_pixel_recognition()
