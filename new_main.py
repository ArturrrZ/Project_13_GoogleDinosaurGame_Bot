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



#detect cactus
def old_version_with_image_recognition():


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


def find_google_icon():
    google = pyautogui.locateCenterOnScreen('google_icon.png', confidence=0.8)

    time.sleep(1)

    pyautogui.click(google.x, google.y)

    time.sleep(1)

    pyautogui.write('https://elgoog.im/dinosaur-game/')
    pyautogui.press('enter')


def new_version_with_pixel_rgb_values():
    time.sleep(3)
    while 1:

        y_positions = [678, 740]
        for each in y_positions:
            r, g, b = pyautogui.pixel(350, each)
            if r < 200:
                pyautogui.press('space')


find_google_icon()
time.sleep(2)

pyautogui.press('space')

end=False
while not end:
    y_positions=[678,740]
    for each in y_positions:
        r, g, b = pyautogui.pixel(350, each)
        if r < 200:
            pyautogui.press('space')