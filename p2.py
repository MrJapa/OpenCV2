import os
import cv2 as cv   
import numpy as np

os.chdir()

haystack_img = cv.imread('albion_farm.jpg', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('cabbage.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

threshold = 0.37
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))
print(locations)

if locations:
    print("Found needle.")
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        cv.rectangle(haystack_img,top_left,bottom_right,line_color,line_type)
    cv.imshow('matches',haystack_img)
    cv.waitKey()
else:
    print("Needle not found")
