import math

import cv2 as cv
import numpy as np

image = cv.imread("Blocks.jpeg")
height, width = image.shape[:2]

CENTER_Y = height/2
CENTER_X = width/2

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

lowerBound = np.array([0, 130, 70])
upperBound = np.array([10, 255, 255]) 
mask = cv.inRange(hsv, lowerBound, upperBound)
contours, n = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # setup

class colorRGB:      # just data class
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

def condition(w,h):
    conA = (400 <= w <= 600) and (800 <= h <= 1200)
    conB = (400 <= h <= 600) and (800 <= w <= 1200)
    return conA or conB
def draw(rect, rgb:colorRGB):
    box = cv.boxPoints(rect)
    box = np.int64(box)
    cv.drawContours(image, [box], 0, (rgb.r, rgb.g, rgb.b), 3)


rects = [[cv.RotatedRect((0.0,0.0), (0.0,0.0), 0.0), math.sqrt((CENTER_X-0.0)**2 + (CENTER_Y-0.0)**2)]]

for contour in contours:
    rect = cv.minAreaRect(contour)
    w, h = rect[1]
    if condition(w,h):
        newRect = [cv.RotatedRect(rect[0], rect[1], rect[2]),math.sqrt((CENTER_X-rect[0][0])**2 + (CENTER_Y-rect[0][1])**2)] # in order in terms of distance to center
        inserted = False
        for i, val in enumerate(rects):
            if newRect[1] <= val[1]:
                rects.insert(i, newRect)
                inserted = True
                break
        if not inserted:
            rects.append(newRect)
        draw(rect, colorRGB(0, 255, 0))

for i in rects:
    print(i[0].center[0],i[0].center[1], i[1])

draw(rects[0][0], colorRGB(255, 0, 0))
outputAngle = rects[0][0].angle
print(outputAngle) # closest to the center and angle to give to differential Rotator

cv.imshow("Blocks", image)
cv.waitKey(0)
cv.destroyAllWindows()