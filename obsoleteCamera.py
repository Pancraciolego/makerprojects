import cv2
import numpy as np

'''
PLEASE READ!

This is the wrong file! This is AI SLOP
My code is very disorganized, I have a lot of projects named yes, other, etc. 
I found this at first thinking it was the right one. It never entirely felt 
right since I remembered I had a single output angle. Now I remember this was written
by AI so I could get a grasp at what a file looked like. I then used the opencv python
documentation to make camera.py

I found camera.py after searching a bit more, after realizing this file looked too sloppy. 
I'm so sorry I did not mean to submit AI Slop.

'''

image = cv2.imread("Blocks.jpeg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_color = np.array([0, 130, 70])   # lower bound of color in HSV
upper_color = np.array([10, 255, 255]) # upper bound of color in HSV
mask = cv2.inRange(hsv, lower_color, upper_color)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    rect = cv2.minAreaRect(contour) 
    x,y = rect[1]
    print(x,y)
    if (x>300) and (y>300):  # checks if box is large enough
        print("2",rect[2])
        print("rect",rect)
        angle = rect[-1]
        if angle<-45:
            angle+=90
        print("angle",rect[-1])  # outpus angles
        box = cv2.boxPoints(rect)  # makes the boxes
        box = np.int64(box)
        cv2.drawContours(image, [box], 0, (0,255,0),2)
        cv2.imshow("Outlined Image", image)
        cv2.waitKey(0)


#cv2.drawContours(image, contours, -1, (250, 250, 250), 2)  # green outline

# Show the output
cv2.imshow("Outlined Image", image)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()