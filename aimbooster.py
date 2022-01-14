import pyautogui
import numpy as np
import time

pyautogui.PAUSE = 0.00001
time.sleep(5)

while True:
    img = pyautogui.screenshot(region=(574,443,748,524))
    open_cv_image = np.array(img)
    for i in range(0,524,10):
        for j in range(0,748,10):
            if open_cv_image[i][j][0] == 255 and open_cv_image[i][j][2] == 195 and open_cv_image[i][j][1] == 219:
                pyautogui.click(574+j,443+i)