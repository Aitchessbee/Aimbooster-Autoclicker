import pyautogui
import cv2
import numpy as np
import time

pyautogui.PAUSE = 0.00001
time.sleep(5)

# Convert RGB to BGR 



# time.sleep(10)

# f = open("aim.txt","w")
# f.write(str(open_cv_image))
# f.close()

while True:
    img = pyautogui.screenshot(region=(574,443,748,524))
    open_cv_image = np.array(img) 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    # cv2.imshow("image",open_cv_image)
    # cv2.waitKey()
    for i in range(0,524,25):
        for j in range(0,748,25):
            if open_cv_image[i][j][2] == 255 and open_cv_image[i][j][0] == 128 and open_cv_image[i][j][1] == 179:
                pyautogui.click(574+j,443+i)

# img = pyautogui.screenshot(region=(574,443,748,524))
# open_cv_image = np.array(img) 
# open_cv_image = open_cv_image[:, :, ::-1].copy()
# # cv2.imshow("image",open_cv_image)
# # cv2.waitKey()
# for i in range(0,524,10):
#     for j in range(0,748,10):
#         print(open_cv_image[i][j], end=" ")
#     print("\n")    